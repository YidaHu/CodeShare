#!/usr/bin/env python
# encoding: utf-8
"""
@author: yida.hu
@contact: yida_hu12@outlook.com
@time: 2021/9/11 14:07
@desc: 获取数据集
"""
# 生成项目用到的 CSV，容易超时，一个个跑
from pandas_datareader import data as wb

# BABA = wb.DataReader('BABA',data_source='yahoo',start='2021-1-4',end='2021-1-29').round(2)
# print(BABA)
# BABA.to_csv(r'BABA.csv',columns=BABA.columns,index=True,sep='\t')

# JD = wb.DataReader('JD',data_source='yahoo',start='2021-1-4',end='2021-1-29').round(2)
# print(JD)
# JD.to_csv(r'JD.csv',columns=JD.columns,index=True,sep='\t')

# TC = wb.DataReader('TCTZF', data_source='yahoo', start='2021-1-4', end='2021-1-29').round(2)
# print(TC)
# TC.to_csv(r'TC.csv', columns=TC.columns, index=True, sep='\t')

EDU = wb.DataReader('EDU', data_source='yahoo', start='2021-1-4', end='2021-1-29').round(2)
print(EDU)
EDU.to_csv(r'EDU.csv', columns=EDU.columns, index=True, sep='\t')