#coding:utf-8
#leetcode 241
#分治算法
def diffWaysToCompute(input):
	if input.isdigit():
		return [int(input)]
	res = []
	for i in xrange(len(input)):
		if input[i] in '-+*':
			res1 = diffWaysToCompute(input[:i])
			res2 = diffWaysToCompute(input[i+1:])
			for j in res1:
				for k in res2:
					res.append(helper(j,k,input[i]))
	return res

def helper(m,n,op):
	if op == '+':
		return m + n
	elif op == '-':
		return m - n
	else:
		return m*n

def test():
	t = "2*3-4*5"
	print diffWaysToCompute(t)


test()
