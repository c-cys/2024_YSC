import cv2
import pandas as pd

video_path = 'assets/test_videos/test_3.mp4'
video = cv2.VideoCapture(video_path)
fps = video.get(cv2.CAP_PROP_FPS)
cv2.namedWindow('Test', cv2.WINDOW_NORMAL)

frame = 0
while video.isOpened():
    check, image = video.read()
    if not check:
        print("Frame Ends.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        break

    df = pd.read_csv('assets/landmark_csv/detection.csv')
    x1 = int(df['x1'][frame])
    y1 = int(df['y1'][frame])
    x2 = int(df['x2'][frame])
    y2 = int(df['y2'][frame])
    print(frame)
    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
    frame += 1

    cv2.imshow('Test', image)
    if cv2.waitKey(1) == ord('q'):
        print("Stopped.")
        break

video.release()
cv2.destroyAllWindows()