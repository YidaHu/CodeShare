#!/usr/bin/env python
# encoding: utf-8
"""
@author: yida.hu
@contact: yida_hu12@outlook.com
@time: 2021/9/14 21:22
@desc:
"""
import numpy as np
import pandas as pd

# 使用多个股票代码，构建新的dataframe
BABA = pd.read_csv('./BABA.csv', sep='\t', index_col=0)
JD = pd.read_csv('./JD.csv', sep='\t', index_col=0)
TC = pd.read_csv('./TC.csv', sep='\t', index_col=0)
EDU = pd.read_csv('./EDU.csv', sep='\t', index_col=0)

stock_data = pd.DataFrame()
stock_data['BABA'] = BABA['Adj Close']
stock_data['JD'] = JD['Adj Close']
stock_data['TCTZF'] = TC['Adj Close']
stock_data['EDU'] = EDU['Adj Close']

# 获取全部股票的每日对数收益率
returns = np.log(stock_data / stock_data.shift(1))
print("每日对数收益率:")
print(returns)

# 输出协方差矩阵
print(returns.cov())
# 输出相关性矩阵
print(returns.corr())

# 获取全部股票的每日简单收益率
simple_returns = round((stock_data / stock_data.shift(1)) - 1, 4)
print("每日简单收益率:")
print(simple_returns)

# 输出协方差矩阵
print(simple_returns.cov())
# 输出相关性矩阵
print(simple_returns.corr())
