import torch
from ultralytics import YOLO
import cv2
import pandas as pd
import os

model = YOLO('weights/best.pt')

test_path = 'assets/test_images'
csv_path = 'assets/landmark_csv/detection.csv'
results_df = pd.DataFrame(columns=['image', 'x1', 'y1', 'x2', 'y2'])

for i in range(0, len(os.listdir(test_path))+1):
    test_name = f'frame_{i}.jpg'
    image_path = os.path.join(test_path, test_name)
    image = cv2.imread(image_path)

    results = model(image)

    for result in results:
        box = result.boxes

        x1, y1, x2, y2 = box.xyxy[0]
        conf = box.conf[0]
        cls = box.cls[0]

        new = pd.DataFrame([{
            'image': int(test_name[6:][:-4]),
            'x1': x1.item(),
            'y1': y1.item(),
            'x2': x2.item(),
            'y2': y2.item()
        }])

        results_df = pd.concat([results_df, new], ignore_index=False)

results_df.to_csv(csv_path, index=False)
print(f'Results saved to {csv_path}.')