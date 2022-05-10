'''
用于读取tsp文件
'''
import pandas as pd
import numpy as np


class Dataloder:
    city_name = []
    city_location = []
    cities = []

    def __init__(self):
        # 载入数据
        df = pd.read_csv('kroA100.tsp', sep=" ", skiprows=6, header=None)
        city = np.array(df[0][0:len(df) - 1])  # 最后一行为EOF，不读入
        self.city_name = city.tolist()

        # print(self.city_name)
        city_x = np.array(df[1][0:len(df) - 1])
        city_y = np.array(df[2][0:len(df) - 1])
        self.city_location = list(zip(city_x, city_y))
        self.cities = [city.astype(np.int32), self.city_location]
        self.cities = np.array(self.cities)
        # print(self.city_location)
