'''
Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''

def longestPalindrome(s):
	longest = 0
	index = 0
	if len(s) == 1:
		return 1,0
	for i in range(len(s)):
		count = 0
		while i-count >= 0 and i+1+count < len(s) and s[i-count] == s[i+1+count]:
			count += 1
		tmp = count * 2
		count = 1
		while i-count >= 0 and i+count < len(s) and s[i-count] == s[i+count]:
			count += 1
		tmp = max(2*count - 1, tmp)
		if tmp > longest:
			index = i
		longest = max(longest, tmp)
	return longest, index


from nose.tools import assert_equal

assert_equal(longestPalindrome('a'),(1,0))
assert_equal(longestPalindrome('aa'),(2,0))
assert_equal(longestPalindrome('aaa'),(3,1))
assert_equal(longestPalindrome('aaaa'),(4,1))
assert_equal(longestPalindrome('aaaaa'),(5,2))
assert_equal(longestPalindrome('baaaaa'),(5,3))
assert_equal(longestPalindrome('aaaaab'),(5,2))
assert_equal(longestPalindrome('abaaaa'),(4,3))
assert_equal(longestPalindrome('aabaaa'),(5,2))
assert_equal(longestPalindrome('aaabaa'),(5,3))
assert_equal(longestPalindrome('aaabaaa'),(7,3))







