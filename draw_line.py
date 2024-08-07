import cv2
import pandas as pd

video_path = 'assets/test_videos/test_3.mp4'
video = cv2.VideoCapture(video_path)
fps = video.get(cv2.CAP_PROP_FPS)
cv2.namedWindow('Line', cv2.WINDOW_NORMAL)

save_path = 'assets/saved_results/test_3/draw_line.mp4'
fourcc = cv2.VideoWriter_fourcc(*'DVIX')
height, width = 360, 640 # 360 640
out = cv2.VideoWriter(save_path, fourcc, fps, (int(width), int(height)))

df = pd.read_csv('assets/landmark_csv/detection.csv')
length = len(df)
frame = 0
while video.isOpened():
    check, image = video.read()
    if not check:
        print("Frame Ends.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        break

    if frame == length-1:
        break

    for i in range(frame):
        x1, y1, x2, y2 = map(int, [df['x1'][i], df['y1'][i], df['x2'][i], df['y2'][i]])
        x3, y3, x4, y4 = map(int, [df['x1'][i + 1], df['y1'][i + 1], df['x2'][i + 1], df['y2'][i + 1]])
        cv2.line(image, (x1, y1), (x3, y3), (0, 0, 255), 3)

    frame += 1
    cv2.imshow('Line', image)
    if cv2.waitKey(1) == ord('q'):
        print("Stopped.")
        break

    out.write(image)

out.release()
video.release()
cv2.destroyAllWindows()