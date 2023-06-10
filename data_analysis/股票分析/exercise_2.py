#!/usr/bin/env python
# encoding: utf-8
"""
@author: yida.hu
@contact: yida_hu12@outlook.com
@time: 2021/9/11 14:41
@desc: 计算投资组合的综合回报率
"""
import numpy as np
import pandas as pd

# 使用多个股票代码，构建新的dataframe
BABA = pd.read_csv('./baba.csv', sep='\t', index_col=0)
JD = pd.read_csv('./jd.csv', sep='\t', index_col=0)
TC = pd.read_csv('./tc.csv', sep='\t', index_col=0)

stock_data = pd.DataFrame()
stock_data['BABA'] = BABA['Adj Close']
stock_data['JD'] = JD['Adj Close']
stock_data['TC'] = TC['Adj Close']

# 获取全部股票的每日简单收益率
returns = stock_data / stock_data.shift(1) - 1
print(returns)

# 设置每个股票的资金占比
weights = np.array([0.3, 0.35, 0.35])
# 通过线性加和，算出综合的简单收益率
combined_return = np.dot(returns, weights)
print(combined_return)
print('年平均的综合简单收益率', round(pd.Series(combined_return).mean() * 250 * 100, 4), '%')
