import cv2

def mouse(window_name):
    mouse_x, mouse_y = None, None
    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(f"Clicked at: ({x}, {y})")
            mouse_x, mouse_y = x, y

    cv2.setMouseCallback(window_name, mouse_callback)
    return (mouse_x, mouse_y)