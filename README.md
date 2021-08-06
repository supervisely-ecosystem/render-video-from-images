<div align="center" markdown>
<img src="https://i.imgur.com/BqAJpRi.png"/>



# Render video from images

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#How-To-Use">How To Use</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/render-presentation-video-from-dataset)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/render-presentation-video-from-dataset)
[![views](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/render-presentation-video-from-dataset&counter=views&label=views)](https://supervise.ly)
[![used by teams](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/render-presentation-video-from-dataset&counter=downloads&label=used%20by%20teams)](https://supervise.ly)
[![runs](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/render-presentation-video-from-dataset&counter=runs&label=runs&123)](https://supervise.ly)

</div>

## Overview

Application creates video from [Supervisely](https://app.supervise.ly) images in the given dataset. You can choose number of images per second for creating a video, labl opacity and thickness of label borders to display images labels on video frames.

**Note:**

Images sizes in dataset must be the same. If one of the images sizes is different from the others, video creating will crash. If images sizes in dataset are different, you can use [resize-images](https://app.supervise.ly/ecosystem/apps/resize-images) application to resize images to the same size.


gallery

<img src="https://i.imgur.com/awCTgKX.png"/>

gif

<img src="https://i.imgur.com/9D6b0f1.mp4"/>


## How To Run 
**Step 1**: Add app to your team from [Ecosystem](https://app.supervise.ly/apps/ecosystem/render-presentation-video-from-dataset) if it is not there.

**Step 2**: Open context menu of dataset -> `Run App` -> `Transform` -> `Render video from images` 

<img src="https://i.imgur.com/cFSJIpi.png"/>

**Step 3**: Select video creating parameters.

<img src="https://i.imgur.com/Iwi6xbu.png" width="500px"/>

## How to use

modal window

<img src="https://i.imgur.com/7CtG24p.png"/>

After running the application, you will be redirected to the `Tasks` page. Once application processing has finished, your link for downloading will be available. Click on the `file name` to download it.

<img src="https://i.imgur.com/crpZvnU.png"/>

**Note:** You can also find your converted project in: `Team Files`->`video_from_images`->`<taskId>` -> `<datasetId>_<datasetName>.mp4`

<img src="https://i.imgur.com/NDEGgnO.png"/>
