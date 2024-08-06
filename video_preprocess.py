from dev import reset
from dev import video_to_images

video_path = 'assets/test_videos/test_3.mp4'
save_path = 'assets/test_images'

reset.reset(save_path)

video_to_images.vid2img(video_path, save_path)