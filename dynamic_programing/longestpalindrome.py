def getLongestPalindrome(s, l, r):
	while l >=0 and r < len(s) and s[l] == s[r]:
		l -=1;
		r += 1;
	return s[l+1:r]

def logestPalindrome(s):
	palindrome = ''
	for i in range(len(s)):
		len1 = len(getLongestPalindrome(s,i,i))
		if len1 > len(palindrome):
			palindrome = getLongestPalindrome(s,i,i)
		len2 = len(getLongestPalindrome(s,i,i+1))
		if len2 > len(palindrome):
			palindrome = getLongestPalindrome(s, i, i+1)
	return palindrome

print logestPalindrome("aabcdcbe")