<div align="center" markdown>
<img src="https://i.imgur.com/2o4AKdp.png"/>



# Render video from images

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Use">How To Use</a> •
  <a href="#Results">Results</a> •
  <a href="#Demo">Demo</a> 
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/render-video-from-images)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/render-video-from-images)
[![views](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/render-video-from-images&counter=views&label=views)](https://supervise.ly)
[![runs](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/render-video-from-images&counter=runs&label=runs&123)](https://supervise.ly)

</div>

# Overview

Convert image **dataset** to **.mp4 downloadable video**. 


Application key points:  
- Images in dataset must be the **same size** (you can use [`Resize images`](https://app.supervise.ly/ecosystem/apps/resize-images))
- Customize FPS
- Customize labels opacity and thickness
 
# How To Use 

1. Add [Render video from images](https://ecosystem.supervise.ly/apps/render-video-from-images) to your team from Ecosystem.

<img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/render-video-from-images" src="https://imgur.com/PboVK7T.png" width="350px" style='padding-bottom: 20px'/>  

2. Run app from the context menu of **Images Project** -> **Dataset**:

<img src="https://imgur.com/0U710SI.png" width="100%"/>

3. Select parameters and press the `Run` button.
 
 
<div align="center" markdown>
<img src="https://i.imgur.com/7CtG24p.png" width="500"/>
</div>


# Results

After running the application, you will be redirected to the `Tasks` page.  
Once application processing has finished, your link for downloading will be available.  
Click on the `file name` to download it.

<img src="https://i.imgur.com/crpZvnU.png"/>

**Note:** You can also find your converted video in:  
`Team Files`->`video_from_images`->`<taskId>` -> `<datasetId>_<datasetName>.mp4`

<img src="https://i.imgur.com/NDEGgnO.png"/>

# Demo
<a data-key="sly-embeded-video-link" href="https://youtu.be/RuyccC1ioss" data-video-code="RuyccC1ioss">
    <img src="https://i.imgur.com/1W3CIbo.png" alt="SLY_EMBEDED_VIDEO_LINK"  style="max-width:100%;">
</a>
