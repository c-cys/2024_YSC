import cv2

def vidshow(video_path):
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)

    while video.isOpened():
        check, image = video.read()
        if not check:
            print("Frame Ends.")
            break

        cv2.namedWindow('Test', cv2.WINDOW_NORMAL)
        cv2.imshow("Test", image)
        if cv2.waitKey(1) == ord('q'):
            print("Stopped.")
            break

    video.release()
    cv2.destroyAllWindows()