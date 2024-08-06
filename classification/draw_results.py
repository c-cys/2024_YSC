import cv2
import pandas as pd
from classification import Classification
from dev.mouse_callback import mouse
video_path = '../assets/test_videos/test_3.mp4'
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

    df = pd.read_csv('../assets/landmark_csv/continuous.csv')
    prev_x1 = df['prev_x1'] ; prev_y1 = df['prev_y1'] ; curr_x1 = df['curr_x1'] ; curr_y1 = df['curr_y1'] ; next_x1 = df['next_x1'] ; next_y1 = df['next_y1']
    # print(frame)
    # cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

    text = 'None'
    if (frame%5 == 3) and (frame >= 13):
        i = (frame - 13)//5 + 3

        raw_points = [(prev_x1[i-1], prev_x1[i-1]), (curr_x1[i-1], curr_y1[i-1]), (next_x1[i-1], next_y1[i-1])]
        points = [(int(prev_x1[i-1]), int(prev_y1[i-1])), (int(curr_x1[i-1]), int(curr_y1[i-1])), (int(next_x1[i-1]), int(next_y1[i-1]))]

        # cv2.circle(image, (int(prev_x1[i-1]), int(prev_y1[i-1])), 5, (0, 0, 255), 5)
        # cv2.circle(image, (int(curr_x1[i-1]), int(curr_y1[i-1])), 5, (0, 0, 255), 5)
        # cv2.circle(image, (int(next_x1[i-1]), int(next_y1[i-1])), 5, (0, 0, 255), 5)

        cv2.line(image, points[0], points[1], (0, 0, 255), 3)
        cv2.line(image, points[1], points[2],(0, 0, 255), 3)

        trajectory = Classification(raw_points)
        if trajectory.is_linear():
            text = 'Linear'
        elif trajectory.is_exponential():
            text = 'Exponential'
        elif trajectory.is_logarithmic():
            text = 'Logarithm'
        else:
            text = 'None'
        print(text)
        cv2.putText(image, text, (30, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1, cv2.LINE_AA)

    frame += 1

    cv2.imshow('Test', image)
    if cv2.waitKey(1) == ord('q'):
        print("Stopped.")
        break

video.release()
cv2.destroyAllWindows()