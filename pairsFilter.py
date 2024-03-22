# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:20:47 2024

@author: Ao Shen
"""

import numpy as np
import pandas as pd
import argparse


# 0.设置参数----
parser = argparse.ArgumentParser(description='To filter the constant values of gene-gene pairs')
parser.add_argument('--input', '-i', type=str, required=True, help='Input an gene-gene pair matrix file name.')
parser.add_argument('--threshold', '-t', type=float, default=0.8, help='Set a filter threshold [0-1]. When this threshold is exceeded, these gene-gene pairs are considered meaningless for subsequent analysis and need to be filtered. Default: 0.8')
parser.add_argument('--output', '-o', type=str, default="pair_filtered.txt", help='Set a output file name. Default: "pair_filtered.txt"')

args = parser.parse_args()


# 1.加载构建好的pairs----
pairs = pd.read_table(args.input, index_col=(0))


# 2.设置过滤阈值并进行过滤----
filterPercent = args.threshold

constantPairs = []
for i in range(len(pairs)):
    constantPairs.append((np.sum(pairs.iloc[i] == 0) / len(pairs.columns) >= filterPercent) | (np.sum(pairs.iloc[i] == 1) / len(pairs.columns) >= filterPercent))

pairs_filters = pairs.drop(pairs[constantPairs].index)


# 3.保存过滤后的pairs----
pairs_filters.to_csv(args.output, sep = '\t')
