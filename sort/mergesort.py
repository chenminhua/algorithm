#coding:utf-8
def mergesort(l):
	if len(l) <=1:
		return l
	mid = len(l)/2
	left = mergesort(l[:mid])
	right = mergesort(l[mid:])
	return merge(left, right)

def merge(left, right):
	res = []
	while len(left) !=0 and len(right) != 0:
		if left[0] < right[0]:
			res.append(left.pop(0))
		else:
			res.append(right.pop(0))
	res += left
	res += right
	return res


import random

a = [random.random() for i in range(40)]
print mergesort(a)