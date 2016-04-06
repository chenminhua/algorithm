def atoi(s):
	if s == "":
		return 0
	import re
	s = s.strip()
	if re.match(r'^[+-]?\d+', str) == None:
		return 0
	str = re.match(r'^[+-]?\d+', str).group()
	MAX_INT = 2147483647
	MIN_INT = -2147483647

	try:
		ret = int(str)
		if ret > MAX_INT:
			return MAX_INT
		elif ret < MIN_INT:
			return MIN_INT
		else:
			return ret
	except:
		return 0