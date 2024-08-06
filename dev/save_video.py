import cv2

def save_video(video_path, save_path, frame):
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')

    height, width, _ = frame.shape
    out = cv2.VideoWriter(save_path, fourcc, fps, (int(width), int(height)))

    out.write(frame)

    out.release()