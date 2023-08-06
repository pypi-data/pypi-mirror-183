'''
Created on Dec 26, 2022
@author: bilal.peerzade
'''

import pandas as pd


def formatSlackMessage(df):
    df = df.applymap(str)
    max_lengths = df.apply(lambda x: (x.str.len().max() if x.str.len().max() > len(x.name) else len(x.name)) if x.dtype == 'object' else len(x.name))
    separator = '+'
    for m in max_lengths:
      separator = separator+ (m+2) *'-' +'+'
    separator = separator +'\n'
    i=0
    header='|'
    for col in df.columns:
      header = header +col+ (max_lengths[i]+2-len(col)) *' '+'|'
      i+=1
    header = header +'\n'
    rows=''
    for element in df.values:
      i=0
      rows=rows+'|'
      for row in element:
        rows = rows+str(row)+(max_lengths[i]+2-len(str(row))) *' '+'|'
        i+=1
      rows=rows+'\n'
    output = separator+header+separator+rows+separator
    return output
