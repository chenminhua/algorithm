#coding:utf-8


def binarySearch(l, value):
	res = -1
	if not l:
		return -1
	if len(l) == 1 and l[0] == value:
		return 0

	start = 0
	end = len(l)
	while start <= end:
		mid = (start + end) / 2		
		if l[mid] == value:
			res = mid
			break
		elif l[mid] > value:
			end = mid -1
		else:
			start = mid + 1
	return res




from nose.tools import assert_equal

def test():
	l = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
	assert_equal(binarySearch(l, 2),0)
	assert_equal(binarySearch(l, 7),3)
	assert_equal(binarySearch(l, 6),-1)


	l = []
	assert_equal(binarySearch(l,1),-1)

	

	print "success"

test()


