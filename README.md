# 2024_YSC
Project for 2024 YSC from GLOBE

Model Pipeline
-
![pipeline.jpg](assets/model_pipeline.jpg)

Description
-
- Final results can be shown in [`/classification/draw_results.py`](classification/draw_results.py)
- [`2024_YSC_Beta.ipynb`](2024_YSC_Beta.ipynb): YOLOv8 Based **Object Detection** Model. GPU needed.
- [`video_preprocess.py`](video_preprocess.py): Converting video to images by frame.
- [`/classfication/`](classification): Classifying trajectory into [linear](classification/linear.py)/[exponential](classification/exp.py)/[logarithm](classification/log.py).
- [`draw_box.py`](draw_box.py): Drawing Bounding Box using object detection results while video playing.
- [`draw_line.py`](draw_line.py): Drawing lines between previous/current/next coordinates while video playing.
- [`draw_trajectory.py`](draw_trajectory.py): Drawing trajectory by leaving trace every 10 frames. & Connecting a line about every coordinates.