import cv2
import os
import globals as g
import supervisely as sly
from supervisely.io.fs import mkdir
from supervisely.project.download import download_async_or_sync
from supervisely import handle_exceptions

@sly.timeit
@handle_exceptions(has_ui=False)
def render_video_from_images(api: sly.Api, task_id):
    work_dir = os.path.join(g.storage_dir, g.working_folder)
    mkdir(work_dir, True)
    download_async_or_sync(
        api, g.PROJECT_ID, work_dir, dataset_ids=[g.DATASET_ID], log_progress=True
    )

    meta_json = sly.json.load_json_file(os.path.join(work_dir, "meta.json"))
    meta = sly.ProjectMeta.from_json(meta_json)

    dataset_info = api.dataset.get_info_by_id(g.DATASET_ID)
    dataset_path = os.path.join(work_dir, dataset_info.name)
    imgs_path = os.path.join(dataset_path, "img")
    anns_path = os.path.join(dataset_path, "ann")

    result_dir = os.path.join(g.storage_dir, g.working_folder)
    mkdir(result_dir)
    video_path = os.path.join(result_dir, dataset_info.name + g.video_ext)
    file_remote = os.path.join(
        sly.team_files.RECOMMENDED_EXPORT_PATH,
        "{}/{}/{}_{}".format(
            g.result_folder, g.TASK_ID, g.DATASET_ID, dataset_info.name + g.video_ext
        ),
    )

    images_infos = api.image.get_list(g.DATASET_ID, sort="name")
    if len(images_infos) == 0:
        sly.logger.warning(
            "There are no images in {} dataset".format(dataset_info.name)
        )
    for idx, image_info in enumerate(images_infos):
        if idx == 0:
            image_shape = (image_info.width, image_info.height)
        elif (image_info.width, image_info.height) != image_shape:
            sly.logger.warning(
                "Sizes of images in {} dataset are not the same. Check your input data.".format(
                    dataset_info.name
                )
            )
            return

    image_names = [image_info.name for image_info in images_infos]
    video = cv2.VideoWriter(
        video_path, cv2.VideoWriter_fourcc(*"MP4V"), int(g.frame_rate), image_shape
    )
    for curr_im_name in image_names:
        curr_im_path = os.path.join(imgs_path, curr_im_name)
        curr_ann_path = os.path.join(anns_path, curr_im_name + g.ann_ext)

        try:
            ann_json = sly.json.load_json_file(curr_ann_path)
            ann = sly.Annotation.from_json(ann_json, meta)
        except Exception as e:
            sly.logger.warning(
                f"Failed to load annotation for image {curr_im_name}: {e}"
            )
            ann = sly.Annotation(img_size=(image_info.height, image_info.width))
        img = cv2.imread(curr_im_path)
        ann.draw_pretty(
            img, opacity=g.label_opacity / 100, thickness=g.border_thickness
        )
        video.write(img)
    video.release()

    upload_progress = []

    def _print_progress(monitor, upload_progress):
        if len(upload_progress) == 0:
            upload_progress.append(
                sly.Progress(
                    message="Upload {!r}".format(file_remote),
                    total_cnt=monitor.len,
                    ext_logger=sly.logger,
                    is_size=True,
                )
            )
        upload_progress[0].set_current_value(monitor.bytes_read)

    sly.logger.info("Local video path: {!r}".format(video_path))
    sly.fs.ensure_base_path(video_path)
    file_info = api.file.upload(
        g.TEAM_ID,
        video_path,
        file_remote,
        lambda m: _print_progress(m, upload_progress),
    )
    api.task.set_output_archive(
        task_id=task_id,
        file_id=file_info.id,
        file_name=sly.fs.get_file_name_with_ext(file_remote),
        file_url=file_info.storage_path,
    )
    sly.logger.info("File successfully uploaded to team files")


def main():
    sly.logger.info(
        "Script arguments", extra={"TEAM_ID": g.TEAM_ID, "WORKSPACE_ID": g.WORKSPACE_ID}
    )
    render_video_from_images(g.api, g.TASK_ID)

if __name__ == "__main__":
    sly.main_wrapper("main", main)
