import pandas as pd

input_csv_path = '../assets/landmark_csv/revised.csv'
output_csv_path = '../assets/landmark_csv/continuous.csv'

df = pd.read_csv(input_csv_path)

new_columns = ['image', 'prev_x1', 'prev_y1', 'prev_x2', 'prev_y2',
               'curr_x1', 'curr_y1', 'curr_x2', 'curr_y2',
               'next_x1', 'next_y1', 'next_x2', 'next_y2']

results = []

for i in range(1, len(df) - 1):
    prev_row = df.iloc[i - 1]
    curr_row = df.iloc[i]
    next_row = df.iloc[i + 1]

    results.append([
        curr_row['image'],
        prev_row['x1'], prev_row['y1'], prev_row['x2'], prev_row['y2'],
        curr_row['x1'], curr_row['y1'], curr_row['x2'], curr_row['y2'],
        next_row['x1'], next_row['y1'], next_row['x2'], next_row['y2']
    ])

results_df = pd.DataFrame(results, columns=new_columns)

results_df.to_csv(output_csv_path, index=False)
print(f'New CSV file saved to {output_csv_path}')