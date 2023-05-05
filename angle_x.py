import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Constants
SAMPLING_FREQ = 100  # Hz
DT = 1 / SAMPLING_FREQ

if __name__ == '__main__':

    gyro_data = pd.read_csv('./data/Gyroscope.csv')
    angle_data = np.cumsum(gyro_data * DT) 

    # Plot angle data
    plt.xlabel('time (s)')
    plt.ylabel('angle x(rad)')
    plt.plot(angle_data['x'])
    
    plt.show()

