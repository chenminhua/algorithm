#coding:utf-8
def insertSort(l, start, gap):
	for i in range(start+gap, len(l), gap):
		currentValue = l[i]
		pos = i
		while pos >= gap and l[pos-gap] > currentValue:
			l[pos] = l[pos - gap]
			pos -= gap
		l[pos] = currentValue

def shellSort(l):
	sublistCount = len(l) / 2
	while sublistCount>0:
		for pos in range(sublistCount):
			insertSort(l, pos, sublistCount)
		sublistCount = sublistCount / 2

import random

a = [random.random() for i in range(40)]
print a
shellSort(a)
print a

