#!/usr/bin/env python
# encoding: utf-8
"""
@author: yida.hu
@contact: yida_hu12@outlook.com
@time: 2021/9/14 21:14
@desc:
"""
import numpy as np
import pandas as pd

# 使用多个股票代码，构建新的dataframe
BABA = pd.read_csv('./baba.csv', sep='\t', index_col=0)
JD = pd.read_csv('./jd.csv', sep='\t', index_col=0)
TC = pd.read_csv('./tc.csv', sep='\t', index_col=0)
EDU = pd.read_csv('./EDU.csv', sep='\t', index_col=0)

stock_data = pd.DataFrame()
stock_data['BABA'] = BABA['Adj Close']
stock_data['JD'] = JD['Adj Close']
stock_data['TCTZF'] = TC['Adj Close']
stock_data['EDU'] = EDU['Adj Close']

# 获取全部股票的每日对数收益率
returns = np.log(stock_data / stock_data.shift(1))
print(returns)

print('阿里巴巴日均对数收益率的方差', round(returns['BABA'].var() * 100, 4), '%')
print('京东日均对数收益率的方差', round(returns['JD'].var() * 100, 4), '%')
print('腾讯日均对数收益率的方差', round(returns['TCTZF'].var() * 100, 4), '%')
print('新东方教育日均对数收益率的方差', round(returns['EDU'].var() * 100, 4), '%')

print('阿里巴巴日均对数收益率的标准差', round(returns['BABA'].std() * 100, 4), '%')
print('京东日均对数收益率的标准差', round(returns['JD'].std() * 100, 4), '%')
print('腾讯日均对数收益率的标准差', round(returns['TCTZF'].std() * 100, 4), '%')
print('新东方教育日均对数收益率的标准差', round(returns['EDU'].std() * 100, 4), '%')

print('阿里巴巴年均对数收益率的方差', round(returns['BABA'].var() * 250 * 100, 4), '%')
print('京东年均对数收益率的方差', round(returns['JD'].var() * 250 * 100, 4), '%')
print('腾讯年均对数收益率的方差', round(returns['TCTZF'].var() * 250 * 100, 4), '%')
print('新东方教育年均对数收益率的方差', round(returns['EDU'].var() * 250 * 100, 4), '%')

print('阿里巴巴年均对数收益率的标准差', round(returns['BABA'].std() * 250 ** 0.5 * 100, 4), '%')
print('京东年均对数收益率的标准差', round(returns['JD'].std() * 250 ** 0.5 * 100, 4), '%')
print('腾讯年均对数收益率的标准差', round(returns['TCTZF'].std() * 250 ** 0.5 * 100, 4), '%')
print('新东方教育年均对数收益率的标准差', round(returns['EDU'].std() * 250 ** 0.5 * 100, 4), '%')
