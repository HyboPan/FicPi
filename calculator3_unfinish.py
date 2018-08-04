#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv # 用于写入 csv 文件


# 处理命令行参数类
class Args(object):
    
    def __init__(self):
        self.args = sys.srgv[1:]
        
        #补充参数读取函数，并返回相应的路径

        #当参数格式出错时，抛出异常
        try:
            num = len(sys.argv)
            num >= 1
        except Exception:
            print("Parameter Error")
            sys.exit(-1)

# 配置文件类
class Config(object):

    def __init__(self):
        self.config = self._read_config()

    #配置文件读取内部函数，并保存到 config 这个字典里
    def _read_config(self):
        config = {}
        pre = 0
        test = '/home/shiyanlou/test.cfg'
        try:
            with open(test, 'r') as cfg_file:
                for cfg_line in cfg_file:
                    config[cfg_line.split(' = ')[0].strip()] = float(cfg_line.split(' = ')[1].strip())
                    pre += cfg_line.split(' = ')[1].strip()
        except:
            print("Parameter Error")
            sys.exit(-1)

        return config and pre
        
# 用户数据类
class UserData(object):

    def __init__(self):
        self.userdata = self.read_users_data()

    # 用户数据读取内部函数
    def _read_users_data(self):
        userdata = []
        ud = '/home/shiyanlou/user.csv'
        try:
            with open(ud, 'r') as ud_file:
                for ud_line in ud_file:
                    ud_num = len(ud_line.split(','))
                    if ud_num == 2 and int(ud_line.strip().split(',')[0]) and int(ud_line.strip().split(',')[1]):
                        pass
                    userdata.append(ud_line.strip())
        except:
            print("Parameter Error")
            sys.exit(-1)
        
        return userdata

# 税后工资计算类
class IncomeTaxCalculator(object):

    # 计算每位员工的税后工资函数
    def calc_for_all_userdata(self):
        for 
        """
        补充代码：
        1. 计算每位员工的税后工资（扣减个税和社保）
        2. 注意社保基数和判断
        3. 将每位员工的税后工资按指定格式返回
        """

    def calculate(wage):
        if wage <= 3500:
            return wage - wage * pre
        elif wage > 3500:
            taxincome = wage - 3500 - wage * 0.165
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
            return wage - taxincome * tr + ed - wage * pre

    def lists():
        for arg in sys.argv[1:]:
            lt = arg.split(':')
            wn = int(lt[0])
            wage = int(lt[1])
            print(format(wn) + "," + format(wage) + "," + format(wage * pre, ".2f") + "," + format(calculate(wage), ".2f"))



    # 输出 CSV 文件函数
    def export(self, default='csv'):
        result = self.calc_for_all_userdata()
        with open("输出文件的路径，由输入参数获得") as f:
            writer = csv.writer(f)
            writer.writerows(result)



def lists():
    for arg in sys.argv[1:]:
        lt = arg.split(':')
        wn = int(lt[0])
        wage = int(lt[1])
        print(format(wn) + "," + format(wage) + "," + format(wage * pre, ".2f") + "," + format(calculate(wage), ".2f"))


if __name__ == "__main__":
   
    lists()
