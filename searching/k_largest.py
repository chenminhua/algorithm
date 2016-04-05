#coding:utf-8
"""
we use a clever algorithm that combines the ideas of binarySearch and quicksort
to arrive at an O(n) solution
"""
def findKthLargest(nums, k):
	return findKthSmallest(nums, len(nums)+1-k)

def findKthSmallest(nums, k):
	if nums:
		pos = partition(nums, 0, len(nums)-1)
		if k > pos + 1:
			return findKthSmallest(nums[pos+1:], k-pos-1)
		elif k < pos + 1:
			return findKthSmallest(nums[:pos], k)
		else:
			return nums[pos]

def partition(nums, l, r):
	#choose the right-most element as pivot
	low = l
	while l < r:
		if nums[l] < nums[r]:
			nums[l], nums[low] = nums[low], nums[l]
			low += 1
		l += 1
	nums[low], nums[r] = nums[r], nums[low]
	return low

from nose.tools import assert_equal

def test():
	test = [4,2,6,7,8,9,12,43,32,21,55,67,24]
	assert_equal(sorted(test)[-4], findKthLargest(test,4))
	

	print "success"

test()

