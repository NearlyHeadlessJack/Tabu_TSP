'''
TSP Benchmark问题求解
使用数据KroA100
初始解随机产生
领域移动方式为2-opt
采用基于概率的邻域搜索方式
惩罚因子设为0.001
采用t-检验的方式分析算法性能
'''
from cgitb import reset
from dataloader import Dataloder
from lists import TList, PList,Cache,Subset
import random,math
from savedata import SaveData
import numpy as np
import time
from search import Search

    
if __name__ == "__main__":
    init_move =[49, 65, 63, 41, 13, 96, 6, 11, 59, 27, 14,100, 44, 42, 54, 98, 73, 84, 75, 36, 34, 99, 58, 30, 82, 21, 80, 53, 31, 71, 57, 56, 38, 43, 94, 50, 78, 19, 66, 28, 61,22, 2, 46, 45, 32, 85, 83, 72, 23, 95, 90, 81, 68, 67, 1,70, 48, 87, 93, 40, 91, 29, 24, 17, 8, 3, 18, 15, 74, 69,64, 9, 26, 77, 51, 10, 79, 60, 88, 47, 5, 89, 20, 25, 35,7, 76, 12, 97, 52, 55, 33, 39, 86, 16, 37, 4, 62, 92]
    save = SaveData()
    s = Search(save, init_move, alpha=0.001 , subset_size=60, epochs=2000, tabu_size=30, is_show=True,
               is_ban_plist=True)
    for i in range(2):
        s.exp()
    save.write_data(True)




    
    


