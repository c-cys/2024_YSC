import pandas as pd

df = pd.read_csv('../assets/landmark_csv/detection.csv')
csv_path = '../assets/landmark_csv/revised.csv'

header = df.iloc[0:1]
data = df.iloc[1:]

averaged_rows = []
for i in range(0, len(data), 5):
    temp = data.iloc[i:i+5]
    temp_mean = temp.mean()
    averaged_rows.append(temp_mean)

result_df = pd.DataFrame(averaged_rows)
result_df = pd.concat([header, result_df], ignore_index=True)

result_df.to_csv(csv_path, index=False)
print(f'New CSV file saved to {csv_path}.')