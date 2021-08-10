<div align="center" markdown>
<img src="https://i.imgur.com/2o4AKdp.png"/>



# Render video from images

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#How-To-Use">How To Use</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/render-video-from-images)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/render-video-from-images)
[![views](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/render-video-from-images&counter=views&label=views)](https://supervise.ly)
[![used by teams](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/render-video-from-images&counter=downloads&label=used%20by%20teams)](https://supervise.ly)
[![runs](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/render-video-from-images&counter=runs&label=runs&123)](https://supervise.ly)

</div>

## Overview

Application creates video from images in the given dataset. You can choose number of images per second for creating a video, label opacity and thickness of label borders to display images labels on video frames. Every image in the given dataset must be the same size. If one of the images is different from the others, video creating will crash, you can use [`Resize images`](https://app.supervise.ly/ecosystem/apps/resize-images) application to resize images to the same size.

**Example:**

<p align="center">
<img src="https://i.imgur.com/awCTgKX.png" width="600"/>
</p>

<p align="center"> <a href="https://imgur.com/9D6b0f1">Result video</a> </p>
  
## How To Run 
**Step 1**: Add app to your team from [Ecosystem](https://app.supervise.ly/apps/ecosystem/render-video-from-images) if it is not there.

**Step 2**: Open context menu of dataset -> `Run App` -> `Transform` -> `Render video from images` 

<img src="https://i.imgur.com/Iwi6xbu.png" width="700"/>

**Step 3**: Select video parameters and press the `Run` button.

<img src="https://i.imgur.com/7CtG24p.png" width="500"/>

## How to use

After running the application, you will be redirected to the `Tasks` page. Once application processing has finished, your link for downloading will be available. Click on the `file name` to download it.

<img src="https://i.imgur.com/crpZvnU.png"/>

**Note:** You can also find your converted video in: `Team Files`->`video_from_images`->`<taskId>` -> `<datasetId>_<datasetName>.mp4`

<img src="https://i.imgur.com/NDEGgnO.png"/>

### Watch Tutorial Video
<a data-key="sly-embeded-video-link" href="https://youtu.be/Xc7iC4glDEo" data-video-code="Xc7iC4glDEo">
    <img src="https://i.imgur.com/1W3CIbo.png" alt="SLY_EMBEDED_VIDEO_LINK"  style="max-width:100%;">
</a>
