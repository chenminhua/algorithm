#coding:utf-8
#这是一个online的算法
#leetcode53题，但是如何使用dc来解决这个问题呢？
def maxSubArray(l):
	if not l:
		return 0
	curSum = maxSum = l[0]
	for num in l[1:]:
		curSum = max(num, curSum+num)
		maxSum = max(curSum, maxSum)
	return maxSum

from nose.tools import assert_equal
def test():
	l = [-2,1,-3,4,-1,2,1,-5,4]
	assert_equal(maxSubArray(l), 6)
	print "success"

test()