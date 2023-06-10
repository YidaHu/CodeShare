#!/usr/bin/env python
# encoding: utf-8
"""
@author: yida.hu
@contact: yida_hu12@outlook.com
@time: 2021/9/11 14:07
@desc: 计算不同类型的收益率和投资组合的收益率
"""
import numpy as np
import pandas as pd

# 获取阿里巴巴2021年1月股价数据
BABA = pd.read_csv('baba.csv', sep='\t', index_col=0)

# 显示最初的几条数据
print('阿里巴巴2021年1月初的股价', BABA.head())

# 显示最后的几条数据
print('阿里巴巴2021年1月底的股价', BABA.tail())

# 获取京东2021年1月股价数据
JD = pd.read_csv('jd.csv', sep='\t', index_col=0)
# 显示最初的几条数据
print('京东2021年1月初的股价', JD.head())
# 显示最后的几条数据
print('京东2021年1月底的股价', JD.tail())

# 获取腾讯2021年1月股价数据
TC = pd.read_csv('tc.csv', sep='\t', index_col=0)
# 显示最初的几条数据
print('腾讯2021年1月初的股价', TC.head())
# 显示最后的几条数据
print('腾讯2021年1月底的股价', TC.tail())

# 获取阿里巴巴的简单收益率
BABA['simple_return'] = round((BABA['Adj Close'] / BABA['Adj Close'].shift(1)) - 1, 4)
print(BABA['simple_return'])

# 获取阿里巴巴的日平均简单收益率
print('阿里巴巴的日平均简单收益率', round(BABA['simple_return'].mean() * 100, 4), '%')
# 获取阿里巴巴的年平均简单收益率
print('阿里巴巴的年平均简单收益率', round(BABA['simple_return'].mean() * 250 * 100, 4), '%')

# 获取阿里巴巴的日平均对数收益率
BABA['log_return'] = round(np.log((BABA['Adj Close'] / BABA['Adj Close'].shift(1))), 4)
print('阿里巴巴的日平均对数收益率', round(BABA['log_return'].mean() * 100, 4), '%')
# 获取阿里巴巴的年平均对数收益率
print('阿里巴巴的年平均对数收益率', round(BABA['log_return'].mean() * 250 * 100, 4), '%')


# 获取京东的简单收益率
JD['simple_return'] = round((JD['Adj Close'] / JD['Adj Close'].shift(1)) - 1, 4)
print(JD['simple_return'])

# 获取京东的日平均简单收益率
print('京东的日平均简单收益率', round(JD['simple_return'].mean() * 100, 4), '%')
# 获取京东的年平均简单收益率
print('京东的年平均简单收益率', round(JD['simple_return'].mean() * 250 * 100, 4), '%')

# 获取京东的日平均对数收益率
JD['log_return'] = round(np.log((JD['Adj Close'] / JD['Adj Close'].shift(1))), 4)
print('京东的日平均对数收益率', round(JD['log_return'].mean() * 100, 4), '%')
# 获取京东的年平均对数收益率
print('京东的年平均对数收益率', round(JD['log_return'].mean() * 250 * 100, 4), '%')


# 获取腾讯的简单收益率
TC['simple_return'] = round((TC['Adj Close'] / TC['Adj Close'].shift(1)) - 1, 4)
print(TC['simple_return'])

# 获取腾讯的日平均简单收益率
print('腾讯的日平均简单收益率', round(TC['simple_return'].mean() * 100, 4), '%')
# 获取腾讯的年平均简单收益率
print('腾讯的年平均简单收益率', round(TC['simple_return'].mean() * 250 * 100, 4), '%')

# 获取腾讯的日平均对数收益率
TC['log_return'] = round(np.log((TC['Adj Close'] / TC['Adj Close'].shift(1))), 4)
print('腾讯的日平均对数收益率', round(TC['log_return'].mean() * 100, 4), '%')
# 获取腾讯的年平均对数收益率
print('腾讯的年平均对数收益率', round(TC['log_return'].mean() * 250 * 100, 4), '%')
