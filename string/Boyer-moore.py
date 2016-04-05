"""
boyer-moore, kmp, sunday, rk
"""
def indexof(s,pattern):
	length = len(pattern)

	skipTable = {}
	for i,c in enumerate(pattern):
		skipTable[c] = length-i-1

	p = length - 1
	lastChar = pattern[-1]

	i = length-1

	def backwards(p,i,s):
		q = p
		j = i
		while q > 0:
			j = j-1
			q = q-1
			if s[j] != pattern[q]:
				return None
		
		return j

	import time
	while i < len(s):
		c = s[i]
		if c == lastChar:
			res = backwards(p,i,s)
			if res == 0:
				return 0
			if res:
				return res
			i += 1
		else:
			if skipTable.has_key(c):
				i += skipTable[c]
			else:
				i += length

s ="abcdeft"
pattern = "de"

print indexof(s,pattern)
print indexof(s,"dff")
print indexof(s, "abc")
