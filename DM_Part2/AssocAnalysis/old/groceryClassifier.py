import numpy
import apriori as ap
from decimal import *
from itertools import groupby
import pandas as pd
import numpy as np

from itertools import combinations
def get_support(df):
    pp = []
    for cnum in range(1, len(df.columns)+1):
        for cols in combinations(df, cnum):
            s = df[list(cols)].all(axis=1).sum()
            pp.append([",".join(cols), s])
    sdf = pd.DataFrame(pp, columns=["Pattern", "Support"])
    return sdf


s = get_support(df)

N = [1,2,2,1,3,3,3,4,4,4,4,5,5,5,5,5,'hi','bye','bye','hi']

# print([list(j) for i, j in groupby(N)])

dataset_file = open('/Users/johnlimjsj/GitHub/EE4483_AI/Part2/Project2/grocery.basket.txt')
lines = dataset_file.read().splitlines()



data = [l.split(',') for l in lines]
# print([list(j) for i, j in groupby(data)])
flat = [item for sublist in data for item in sublist]
itemlist= list(set(flat))
itemlist.sort()
print itemlist
itemlist = dict((item,0) for item in itemlist)
print itemlist

for line in lines:
	for item in itemlist:
		if set(item).issubset(set(line)):
			itemlist[item]+=1

print itemlist

total = sum(len(x) for x in data)
maximum = max(len(x) for x in data)
maxItemSets = pow(2,total) -1
assocRules = pow(3, total) - pow(2, total+1) +1

print "max size: ", maximum
print "total: ", total
print "Max number of itemsets: ", '%.2E' % Decimal(maxItemSets)
print "Max association rules: ", '%.E' % Decimal(assocRules)


for d in data:
	d.sort()


data.sort()
data.sort(key=len)



item = [[] for i in range(1,11)]

for i in range(1,10):
	for d in data:
		if len(d)==i:
			item[i].append(d)



ordered = [list(j) for i, j in groupby(data)]



# print ordered

