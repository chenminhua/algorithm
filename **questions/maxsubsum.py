"""
leetcode 53
https://leetcode.com/problems/maximum-subarray/
"""

def maxSub(arr):
	count = arr[0]
	res = arr[0]
	for a in arr[1:]:
		count = max(a,count+a)
		res = max(res,count)
	return res

