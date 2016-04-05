#coding:utf-8
w = [0,1,2,5,6,7]
v = [0,1,6,18,22,28]
C = 11

w_count = len(w)

m = [[0 for i in range(C+1)] for i in range(w_count)]

x = [0 for i in range(1,w_count)]

for i in range(1, w_count):
	for j in range(C + 1):
		if w[i] > j:
			m[i][j] = m[i-1][j]
		else:
			m[i][j] = max(m[i-1][j], m[i-1][j-w[i]] + v[i])

for row in m:
	print row
