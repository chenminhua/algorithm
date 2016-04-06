def allRange(s):
	if len(s) == 1:
		return s[0]
	res = map(lambda x : s[0] + x, allRange(s[1:]))
	for i in range(1,len(s)):
		tmp = [n for n in s]
		tmp[0], tmp[i] = tmp[i],tmp[0]
		s = ''.join(tmp)
		res += map(lambda x : s[0] + x, allRange(s[1:]))
	return res

a="abcde"

print allRange(a)  #5! = 120