'''
@文件名:savedata.py
@描述:保存数据和文件的类
@author:NearlyHeadlessJack@rjack.cn
@comment:save方法保存数据,write_data方法写文件
'''
class SaveData:
    exp_result = []
    exp_tsize = []
    exp_isBan = []
    exp_optimum = []
    exp_total = []
    
    def __init__(self) :
        return 
    
    def save(self,tsize,isBan,dis,times):
        self.exp_tsize.append(tsize)
        self.exp_isBan.append(isBan)
        self.exp_optimum.append(dis)
        self.exp_total.append(times)
        
        
    def write_data(self,isShow=False):
        self.exp_result.append(self.exp_tsize)
        self.exp_result.append(self.exp_isBan)
        self.exp_result.append(self.exp_optimum)
        self.exp_result.append(self.exp_total)
        if isShow: 
            print(self.exp_result)
            
        with open(file = 'tisze.txt',mode = 'w+')as f:
            for exp in self.exp_result[0]:
                f.writelines(str(exp)+'\n')
        
        with open(file = 'isBan.txt',mode = 'w+')as f:
            for exp in self.exp_result[1]:
                f.writelines(str(exp)+'\n')
        with open(file = 'dis.txt',mode = 'w+')as f:
            for exp in self.exp_result[2]:
                f.writelines(str(exp)+'\n')
        with open(file = 'times.txt',mode = 'w+')as f:
            for exp in self.exp_result[3]:
                f.writelines(str(exp)+'\n')
    