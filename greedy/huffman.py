#coding:utf-8
#huffman编码

from heapq import heapify, heappush, heappop
from itertools import count

def huffman(seq, frq):
	num = count()
	trees = list(zip(frq,num,seq))    #num ensures valid ordering
	heapify(trees)                    #A min-heap based on freq
	while len(trees) > 1:             #until all are combinedi
		fa, _, a = heappop(trees)     #get the two smallest trees
		fb, _, b = heappop(trees)  
		print a,b   
		n = next(num)
		heappush(trees, (fa+fb, n, [a,b]))  #combine and re-add them
	return trees[0][-1]

seq = "abcdefghi"
frq = [4,5,6,9,11,12,15,16,20]
print huffman(seq,frq) 