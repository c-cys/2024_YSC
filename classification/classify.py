import pandas as pd
from classification import Classification

df = pd.read_csv('../assets/landmark_csv/continuous.csv')
prev_x1 = df['prev_x1'] ; prev_y1 = df['prev_y1'] ; curr_x1 = df['curr_x1'] ; curr_y1 = df['curr_y1'] ; next_x1 = df['next_x1'] ; next_y1 = df['next_y1']

for i in range(1, len(df)):
    points = [(prev_x1[i], prev_x1[i]), (curr_x1[i], curr_y1[i]), (next_x1[i], next_y1[i])]
    trajectory = Classification(points)
    if trajectory.is_linear():
        print("The trajectory is linear.")
    elif trajectory.is_exponential():
        print("The trajectory is exponential.")
    elif trajectory.is_logarithmic():
        print("The trajectory is logarithmic.")
    else:
        print("The trajectory does not fit any of the predefined models.")