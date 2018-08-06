#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv # 用于写入 csv 文件


# 处理命令行参数类
class Args:
    
    def __init__(self):
        self.args = sys.argv[1:]
        
        #读取函数，并返回相应的路径
        try:
            for arg in self.args:
                if '-c' and '-d' and '-o' in arg:
                    self.c = self.args[1]
                    self.d = self.args[3]
                    self.o = self.args[5]
        except Exception:
            print("Parameter Error")
            sys.exit(-1)
    c = '' #配置文件路径
    d = '' #用户文件路径
    o = '' #工资导出路径


# 配置文件类
class Config:

    def __init__(self):
        self.config = self._read_config()

    #配置文件读取内部函数，并保存到 config 这个字典里
    def _read_config(self):
        con = {'s': 0}
        test = Args()
        try:
            with open(test.c, 'r') as cfg_file:
                for cfg_line in cfg_file.readlines():
                    a = cfg_line.split(' = ')[0].strip()
                    b = cfg_line.split(' = ')[1].strip()
                    if a == 'JiShuL' or a == 'JiShuH':
                        con[a] = b
                    else:
                        con['s'] += float(b)
        except:
            print("Parameter Error2")
            sys.exit(-1)

        return con

configs = Config()
print(configs.config)    
    
# 用户数据类
class UserData:

    def __init__(self):
        self.userdata = self.read_users_data()

    # 用户数据读取内部函数
    def read_users_data(self):
        userdata = []
        ud = Args()
        try:
            with open(ud.d, 'r') as ud_file:
                for ud_line in ud_file:
                    ud_num = len(ud_line.split(','))
                    if ud_num == 2 and int(ud_line.strip().split(',')[0]) and int(ud_line.strip().split(',')[1]):
                        pass
                    userdata.append(ud_line.strip())
        except:
            print("Parameter Error")
            sys.exit(-1)
        
        return userdata
ud = UserData()
print(ud.userdata)
    
# 税后工资计算
def calc():
    udata = UserData()
    conf = Config()
    conf.config 
    l = []
    nu = []
    JiShuL = float(conf.config['JiShuL'])
    JiShuH = float(conf.config['JiShuH'])
    pre = float(conf.config['s'])
    for usd in udata.userdata:
        wn = usd.split(',')[0]
        wage = int(usd.split(',')[1])
        if wage <= JiShuL:
           insurance = JiShuL * pre
           pay = 0
        elif JiShuL < wage <= 3500:
            insurance = wage * pre
            pay = 0
        elif JiShuH >= wage > 3500:
            taxincome = wage - 3500 - wage * pre
            if taxincome <= 1500:
                tr = 0.03
                ed = 0
            elif 1500 < taxincome <= 4500:
                tr = 0.10
                ed = 105
            elif 4500 < taxincome <= 9000:
                tr = 0.20
                ed = 555
            elif 9000 < taxincome <= 35000:
                tr = 0.25
                ed = 1005
            elif 35000 < taxincome <= 55000:
                tr = 0.30
                ed = 2755
            elif 55000 < taxincome <= 80000:
                tr = 0.35
                ed = 5505
            elif 80000 < taxincome:
                tr = 0.45
                ed = 13505
            insurance = wage * pre
            pay = taxincome * tr -ed
        elif JiShuH < wage:
            insurance = JiShuH * pre
            taxincome = wage - 3500 - insurance
            tr = 0.45
            ed = 13505
            pay = taxincome * tr -ed
        afwage = wage - pay - insurance
 
        l.append(wn)
        l.append(wage)
        l.append("{:.2f}".format(insurance))
        l.append("{:.2f}".format(pay))
        l.append("{:.2f}".format(afwage))
        nu.append(l)
    return nu

# 输出 CSV 文件函数
def export():  
    result = calc()
    gongzi = Args()
    with open(gongzi.o, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(result)


if __name__ == "__main__":
    export()
   
    
