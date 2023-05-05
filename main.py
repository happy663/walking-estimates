import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal


# Constants
ACC_FILE_PATH = './data/Accelerometer.csv'
GYRO_FILE_PATH = './data/Gyroscope.csv'
SAMPLING_FREQ = 100  # Hz
DT = 1 / SAMPLING_FREQ 
STEP_LENGTH = 30  # cm


def search_peek_time(file_path):
    df = pd.read_csv(file_path)
    df['norm'] = (df['x']**2 + df['y']**2 + df['z']**2)**0.5
    df['low_norm'] = df['norm'].rolling(window=10).mean()
    # ピークを検出
    peek, _ = signal.find_peaks(df['low_norm'], height=12)
    ## peekのtを取得
    peek_t = df['t'][peek]

    return np.round(peek_t,2)



if __name__ == '__main__':
    gyro_data = pd.read_csv(GYRO_FILE_PATH)
    # 't'列を除外したデータを取得
    gyro_data_no_t = gyro_data.drop(columns=['t'])
    # 'x', 'y', 'z'列のみを積分
    angle_data_no_t = np.cumsum(gyro_data_no_t * DT)
    # 積分したデータに't'列を結合
    angle_data = pd.concat([gyro_data['t'], angle_data_no_t], axis=1)
    angle_data['rounded_t'] = np.round(angle_data['t'], 2)
    # search_peek_time()のkeysを取得
    peek_t_values = search_peek_time(ACC_FILE_PATH).values
    angle_data_peek = angle_data[angle_data['rounded_t'].isin(peek_t_values)]
    angle_data_peek_x = angle_data_peek['x']
    
    x_displacement = STEP_LENGTH * np.cos(angle_data_peek_x)
    y_displacement = STEP_LENGTH * np.sin(angle_data_peek_x)
    x_cumulative = np.cumsum(x_displacement)
    y_cumulative = np.cumsum(y_displacement)
    # 初期座標(0,0)が描画されるように挿入
    x_cumulative = np.insert(x_cumulative, 0, 0)
    y_cumulative = np.insert(y_cumulative, 0, 0)
    
    plt.figure()
    plt.plot(x_cumulative, y_cumulative, marker='o')
    x_max = max(x_cumulative)
    y_max = max(y_cumulative)
    #軸を揃える
    plt.xlim(0,max(x_max,y_max)+10)
    plt.ylim(0,max(x_max,y_max)+10)
    plt.xlabel('X Displacement (cm)')
    plt.ylabel('Y Displacement (cm)')
    plt.title('Cumulative X and Y Displacement')
    plt.grid()
    plt.show()