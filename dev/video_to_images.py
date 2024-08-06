import cv2
import os

def vid2img(video_path, save_path):
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)

    count = 0
    while video.isOpened():
        check, frame = video.read()
        if not check:
            print("Frame Ends.")
            break

        file_name = os.path.join(save_path, f'frame_{count}.jpg')
        cv2.imwrite(file_name, frame)
        print(f'frame_{count}.jpg saved.')
        count += 1

        cv2.namedWindow('Test', cv2.WINDOW_NORMAL)
        cv2.imshow("Test", frame)
        if cv2.waitKey(1) == ord('q'):
            print("Stopped.")
            break

    video.release()
    cv2.destroyAllWindows()