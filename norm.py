import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':

    df = pd.read_csv('./data/Accelerometer.csv')
    # normを計算
    df['norm'] = (df['x']**2 + df['y']**2 + df['z']**2)**0.5
    plt.plot(df['t'], df['norm'], zorder=1)
    plt.xlabel('time(s)')
    plt.ylabel('norm\n(m/s^2)', rotation=0, ha='right', va='top')
    # Y軸ラベルの位置を調整
    plt.gca().yaxis.set_label_coords(0, 1.1)
    plt.show()