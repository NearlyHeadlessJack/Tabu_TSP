'''
@文件名:lists.py
@描述:禁忌表类TList 频数表类PList
@author:NearlyHeadlessJack@rjack.cn
@comment1:禁忌表大小可以在实例化对象时指定,也可以使用change_size方法修改
@comment2:禁忌表是一个队列(queue)
@comment3:禁忌表和频数表储存的元素都是集合(set)，例如：{1,3},{2,5}
'''

import numpy as np


# 禁忌表类的实现 ========================
class TList:
    list = []
    max_length = 3  # 禁忌表长度
    
    def __init__(self,length):
        self.list=[]
        for i in range(0,length):
            self.list.append({0,0})
        self.max_length = length
        return
    
    def change_size(self,length):
        self.list=[]
        for i in range(0,length):
            self.list.append({0,0})
        self.max_length = length
        return
        
    
    def search(self,obj):
        for list in self.list:
            if(list == obj):
                return True
        return False

    def iter(self,obj):
        for i in range(1,self.max_length):
            self.list[self.max_length-i] = self.list[self.max_length-i-1]
        self.list[0] = obj
        
    def __del__(self):
        self.list = []
        
# 频数表类的实现 ========================
class PList:
    best = 0 # 渴望水平
    map = [[],[]]
    
    def __init__(self):
        self.map = [[],[]]
        return
    
    def iter(self,obj,isBan=False):
        if isBan:
            return 0
        for set in self.map[0]:
            if set == obj:
                return self.map[0].index(set)
        return 0
                    

    
    def add(self,obj):
        index = self.iter(obj)
        if index == 0:
            self.map[0].append(obj)
            self.map[1].append(1)
        else:
            self.map[1][index] += 1