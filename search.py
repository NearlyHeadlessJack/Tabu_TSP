'''
@文件名:search.py
@描述:搜索策略所在的类
@author:NearlyHeadlessJack@rjack.cn
@comment1:在实例化对象时确定禁忌表大小、惩罚因子、迭代次数、是否使用频数表、随机子集大小等参数
'''
from savedata import SaveData
from lists import *
from dataloader import *
import numpy as np
from numpy import random
from numpy import sqrt
from time import sleep
from copy import deepcopy


class Search:

    def __init__(self, save_data, init_cities, alpha=0.001 , subset_size=80, epochs=200, tabu_size=5,
                 is_show=True, is_ban_plist=False):
        self.saveData = save_data
        self.tabu_list = TList(tabu_size)
        self.p_list = PList()
        dataloader = Dataloader()
        self.original_city = dataloader.cities
        self.city_copy = dataloader.cities
        self.epochs = epochs
        self.subset_size = subset_size
        self.alpha = alpha
        self.optimum = 50000
        self.now_distance = 0
        self.maxsetp = 0
        self.tabu_size = tabu_size
        self.is_show = is_show
        self.is_ban_plist = is_ban_plist

    # 用来生成随机初始路径的方法
    def randommov(self, route_now):
        r = deepcopy(route_now)
        exchange_cities = random.choice(r[0], 2) - 1
        ex = deepcopy(exchange_cities)

        r[1][ex[0]], r[1][ex[1]] = r[1][ex[1]], r[1][ex[0]]

        r[0][ex[0]], r[0][ex[1]] = r[0][ex[1]], r[0][ex[0]]

        return r
    # 随机移动(opt-2方法)
    def random_mov(self, route_now):
        r = deepcopy(route_now)
        exchange_cities = random.choice(r[0], 2) - 1
        ex = deepcopy(exchange_cities)

        r[1][ex[0]], r[1][ex[1]] = r[1][ex[1]], r[1][ex[0]]

        r[0][ex[0]], r[0][ex[1]] = r[0][ex[1]], r[0][ex[0]]

        return r, int(ex[0]), int(ex[1])
    
    # 计算目前路径的长度
    def distance_calculation(self, route_now):

        r = deepcopy(route_now)
        distance = 0.0
        for i in range(1, 100):
            distance += (((r[1][i][0] - r[1][i - 1][0]) ** 2) + ((r[1][i][1] - r[1][i - 1][1]) ** 2)) ** 0.5
        distance += (((r[1][99][0] - r[1][0][0]) ** 2) + ((r[1][99][1] - r[1][0][1]) ** 2)) ** 0.5

        return distance
    
    # 单次搜索的策略
    def search_once(self, route_now):
        subset_size = self.subset_size
        route = deepcopy(route_now)

        print(self.now_distance)

        random_subsets = []
        subsets_distance = []
        random_movsets = []

        for i in range(subset_size):
            route_, mov1, mov2 = self.random_mov(route)
            random_movsets.append({mov1, mov2})
            random_subsets.append(route_)
            distance = self.distance_calculation(route_)
            subsets_distance.append(
                distance + self.alpha * distance * self.p_list.iter({mov1, mov2},self.is_ban_plist))

        random_subsets = np.array(random_subsets)
        subsets_distance = np.array(subsets_distance)

        index_of_order = np.argsort(subsets_distance, axis=0)

        for j in range(subset_size):
            ordered_index = index_of_order[j]
            _set = random_movsets[ordered_index]
            _distance = subsets_distance[ordered_index]
            _subset = random_subsets[ordered_index]
            
            if not self.tabu_list.search(_set):
                self.tabu_list.iter(_set)
                self.now_distance = _distance

                if self.now_distance < self.optimum:
                    self.optimum = self.now_distance
                return _subset

            else:
                print('in')
                if _distance < self.optimum:
                    self.tabu_list.iter(_set)
                    self.now_distance = _distance
                    self.optimum = self.now_distance
                    return _subset
                else:
                    continue
        return route_now
    
    # 生成随机初始路径
    def random_begin(self):
        route = deepcopy(self.original_city)
        for i in range(30):
            route = self.randommov( route)
        return route

    # 搜索
    def search(self):

        self.tabu_list = TList(self.tabu_size)
        self.p_list = PList()
        self.now_distance = self.distance_calculation(self.city_copy)
        self.optimum = self.distance_calculation(self.city_copy)
        epochs = self.epochs
        route = deepcopy(self.city_copy)
        for i in range(epochs):

            route = deepcopy(self.search_once(route))
            if self.now_distance < 42000:
                print("stop epoch:")
                print(i)
                self.saveData.save(self.tabu_size, self.is_ban_plist, self.now_distance, i)
                break

        print("best:")
        print(self.optimum)
        print("latest:")
        print(self.now_distance)
        
    # 实验（如果你要使用同一个初始路径进行分组搜索）
    def exp(self):
        self.city_copy = self.random_begin()

        self.is_ban_plist = False
        self.search()
        self.is_ban_plist = True
        self.search()



