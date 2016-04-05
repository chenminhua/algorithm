def lengthOfLongestSubstring(s):
	res = 0
	cur = 0
	d = {}
	for i, c in enumerate(s):
		if c not in d:
			cur += 1
		else:
			cur = min(i-d[c], cur + 1)
		d[c] = i
		res = max(cur,res)
	return res

from nose.tools import assert_equal

def test():
	s = "aabcdefcde"
	assert_equal(lengthOfLongestSubstring(s),6)
	print "success"

test()