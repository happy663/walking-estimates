import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    gyro_data = pd.read_csv('./data/Gyroscope.csv')
    plt.xlabel('time (s)')
    plt.ylabel('rad/s')
    plt.plot(gyro_data['x'])
    plt.show()