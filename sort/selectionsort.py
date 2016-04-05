#coding:utf-8
def selectionSort(l):
	for i in range(len(l)-1):
		lowest = l[i]
		p = i
		for j in range(1,len(l)-i):
			if l[i+j] < lowest:
				lowest = l[i+j]
				p = i + j
		if p != i:
			l[p],l[i] = l[i],l[p]

import random

a = [random.random() for i in range(40)]
selectionSort(a)
print a



			 
