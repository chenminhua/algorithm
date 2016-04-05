def findsubarraywithsamesum(arr, sum):
	if not arr:
		return []
	if arr[0] == sum:
		return [[sum]] + findsubarraywithsamesum(arr[1:],sum)
	if arr[0] >= sum:
		return []
	return map(lambda x : x+[arr[0]], findsubarraywithsamesum(arr[1:],sum-arr[0]))+ findsubarraywithsamesum(arr[1:],sum)

a = [10,5,5,3,2]
print findsubarraywithsamesum(a,15)

