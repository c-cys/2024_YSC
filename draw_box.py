import cv2
import pandas as pd

video_path = 'assets/test_videos/test_3.mp4'
video = cv2.VideoCapture(video_path)
fps = video.get(cv2.CAP_PROP_FPS)
cv2.namedWindow('Box', cv2.WINDOW_NORMAL)

save_path = 'assets/saved_results/test_3/draw_box.mp4'
fourcc = cv2.VideoWriter_fourcc(*'DVIX')
height, width = 360, 640 # 360 640
out = cv2.VideoWriter(save_path, fourcc, fps, (int(width), int(height)))

df = pd.read_csv('assets/landmark_csv/detection.csv')
frame = 0
while video.isOpened():
    check, image = video.read()
    if not check:
        print("Frame Ends.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        break

    x1 = int(df['x1'][frame])
    y1 = int(df['y1'][frame])
    x2 = int(df['x2'][frame])
    y2 = int(df['y2'][frame])
    print(frame)
    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
    frame += 1

    cv2.imshow('Box', image)
    if cv2.waitKey(1) == ord('q'):
        print("Stopped.")
        break

    out.write(image)

out.release()
video.release()
cv2.destroyAllWindows()