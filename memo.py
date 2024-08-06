import cv2
import pandas as pd
import numpy as np

# 비디오 및 CSV 파일 경로 설정
video_path = 'assets/test_videos/test_3.mp4'
csv_path = 'assets/landmark_csv/detection.csv'

# 비디오 캡처 객체 생성
video = cv2.VideoCapture(video_path)
fps = video.get(cv2.CAP_PROP_FPS)
cv2.namedWindow('Trajectory', cv2.WINDOW_NORMAL)

# CSV 파일 읽기
df = pd.read_csv(csv_path)
length = len(df)
frame = 0

# 첫 번째 프레임 읽기 및 초기화
ret, first_frame = video.read()
if not ret:
    print("Error: Failed to read the first frame from the video.")
    video.release()
    cv2.destroyAllWindows()
    exit()

# 선을 그릴 빈 이미지 생성 (첫 번째 프레임과 동일한 크기)
trajectory_image = np.zeros_like(first_frame)

while video.isOpened():
    check, image = video.read()
    if not check:
        print("Frame Ends.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        break

    if frame >= length - 1:
        break

    # 현재 프레임과 다음 프레임의 좌표 가져오기
    x1, y1, x2, y2 = map(int, [df['x1'][frame], df['y1'][frame], df['x2'][frame], df['y2'][frame]])
    x3, y3, x4, y4 = map(int, [df['x1'][frame + 1], df['y1'][frame + 1], df['x2'][frame + 1], df['y2'][frame + 1]])

    # 선을 빈 이미지에 그림
    cv2.line(trajectory_image, (x1, y1), (x3, y3), (0, 0, 255), 3)

    # 원본 이미지와 합성
    combined_image = cv2.addWeighted(image, 1, trajectory_image, 1, 0)

    frame += 1

    # 결과 이미지 출력
    cv2.imshow('Trajectory', combined_image)
    if cv2.waitKey(1) == ord('q'):
        print("Stopped.")
        break

# 자원 해제 및 윈도우 종료
video.release()
cv2.destroyAllWindows()
