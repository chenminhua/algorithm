def longestSubWithoutRepeat(s):
	d = {}
	result = 0
	cur = 0
	for i,c in enumerate(s):
		if c not in d:
			cur += 1
		else:
			cur = min(cur + 1, i-d[c])
		d[c] = i
		result = max(cur,result)
	return result

	