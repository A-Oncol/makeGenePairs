# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:41:59 2023

@author: Ao Shen
"""

import pandas as pd
import argparse


# 0.设置参数
parser = argparse.ArgumentParser(description='To make a gene-gene pair matrix')
parser.add_argument('--expr', '-e', type=str, required=True, help='Input an expression file name, with genes in row and samples in column.')
parser.add_argument('--output', '-o', type=str, default="pair.txt", help='Set a output file name. Default: "pair.txt"')

args = parser.parse_args()


# 1.读取表达谱数据集
trainSet = pd.read_table(args.expr, index_col=(0))
pair_result = []


# 2.比较
for i in range(len(trainSet)):
    for j in range(i + 1, len(trainSet)):
        pair_result.append(trainSet.iloc[i] > trainSet.iloc[j])

final_result = pd.DataFrame(pair_result)


# 3.添加行名
geneA = []
geneB = []
pairName = []
for i in range(len(trainSet)):
    for j in range(i + 1, len(trainSet)):
        geneA = trainSet.index[i]
        geneB = trainSet.index[j]
        pairName.append(geneA + "|" + geneB)

final_result.index = pairName
final_result.head()


# 4.转为0-1矩阵
df = final_result
for u in df.columns:
    if df[u].dtype == bool:
        df[u] = df[u].astype('int')
df.head()


# 5.输出
df.to_csv(args.output, sep = '\t')
