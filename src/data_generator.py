import pandas as pd
import numpy as np

# read the dataset into python from a GitHub URL
url = 'https://raw.githubusercontent.com/janmayer15/manufacturing-data-stream-simulation-with-Kafka/main/data/wafer_data_sum_cpk.csv'
df = pd.read_csv(url, delimiter=';')
# df = df.drop(columns=['Unnamed: 0'])

def generate_message() -> dict:
    random_row = np.array(df.sample(n=1))
    random_row = random_row.tolist()
    
    return {
        'response': random_row[0][1],
        'Cpk': random_row[0][2],
        'Cpk_class': random_row[0][3],
        'Product_class': random_row[0][4],
        'sum_sensor1': random_row[0][5],
        'sum_sensor2': random_row[0][6],
        'sum_sensor3': random_row[0][7],
        'sum_sensor4': random_row[0][8],
        'sum_sensor5': random_row[0][9],
        'sum_sensor7': random_row[0][10],
        'sum_sensor49': random_row[0][11]
    }

