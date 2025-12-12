import os
import supervisely as sly

api = sly.Api.from_env()

TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])
PROJECT_ID = int(os.environ['modal.state.slyProjectId'])
DATASET_ID = int(os.environ['modal.state.slyDatasetId'])
TASK_ID = int(os.environ["TASK_ID"])

storage_dir = sly.app.get_data_dir()
result_folder = 'video_from_images'
working_folder = 'working_folder'
video_ext = '.mp4'
ann_ext = '.json'
logger = sly.logger

frame_rate = os.environ['modal.state.frameRate']
label_opacity = int(os.environ['modal.state.opacity'])
border_thickness = int(os.environ['modal.state.thickness'])
