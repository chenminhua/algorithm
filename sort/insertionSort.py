#coding:utf-8
#in-place的算法
def insertionSort(l):
	for i in range(1,len(l)):
		tmp = l[i]
		j = i
		while j>0 and tmp < l[j-1]:
			l[j] = l[j-1]
			j -= 1
		l[j] = tmp

import random

a = [random.random() for i in range(40)]
insertionSort(a)
print a