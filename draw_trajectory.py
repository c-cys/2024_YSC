import cv2
import numpy as np
import pandas as pd
import os

image_folder = 'assets/test_images/'
length = len(os.listdir(image_folder))
csv_path = 'assets/landmark_csv/detection.csv'
df = pd.read_csv(csv_path)

bird_boxes = dict()
for i in range(length):
    bird_boxes[f'frame_{i}'] = (df['x1'][i], df['y1'][i], df['x2'][i], df['y2'][i])

first_image = cv2.imread(image_folder + f'frame_0.jpg')
image_height, image_width, _ = first_image.shape

combined_image = np.full((image_height, image_width, 3), (0, 255, 0), dtype=np.uint8)

for i in range(length):
    image = cv2.imread(image_folder + f'frame_{i}.jpg')
    x1, y1, x2, y2 = map(int, bird_boxes[f'frame_{i}'])

    if i%10:
        continue
    cropped_image = image[y1:y2, x1:x2]
    combined_image[y1:y2, x1:x2] = cropped_image

for i in range(length-1):
    result_df = pd.read_csv('classification/result.csv')
    if i in result_df['linear'].values:
        color = (255, 0, 0)
    elif i in result_df['exp'].values:
        color = (0, 0, 0)
    elif i in result_df['log'].values:
        color = (255, 255, 255)
    else:
        color = (0, 0, 255)

    image = cv2.imread(image_folder + f'frame_{i}.jpg')
    x1, y1, x2, y2 = map(int, bird_boxes[f'frame_{i}'])
    x3, y3, x4, y4 = map(int, bird_boxes[f'frame_{i+1}'])
    cv2.line(combined_image, (x1, y1), (x3, y3), color, 3)

cv2.imwrite('assets/saved_results/test_3/trajectory.jpg', combined_image)
cv2.namedWindow('Trajectory', cv2.WINDOW_NORMAL)
cv2.imshow('Trajectory', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()