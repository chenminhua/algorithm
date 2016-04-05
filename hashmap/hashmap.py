#coding:utf-8
"""
用list来实现dicts(hashmap)
http://learnpythonthehardway.org/book/ex39.html
"""
def new(num_buckets=256):
	"""initializes a map with the given number of buckets"""
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap

def hash_key(aMap, key):
	return hash(key) % len(aMap)

def get_bucket(aMap, key):
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]

def get_slot(aMap, key, default=None):
	"""
	return index,key,value of a slot found in a buckets
	return -1,key,default (None if not set) when not found
	"""
	bucket = get_bucket(aMap,key)
	for i,kv in enumerate(bucket):
		k,v = kv   #kv is a tuple
		if key == k:
			return i, k, v
	return -1, key, default

def get(aMap, key, default=None):
	i,k,v = get_slot(aMap, key, default=default)
	return v

def set(aMap, key, value):
	bucket = get_bucket(aMap, key)
	i,k,v = get_slot(aMap, key)

	if i >= 0:
		bucket[i] = (key, value)
	else:
		bucket.append((key,value))

def delete(aMap, key):
	bucket = get_bucket(aMap, key)
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break



def list(aMap):
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k,v


"""
注意：
理想情况下我们希望任何两个不同的关键字被映射到不同的单元。
不过，这是不可能的。因为单元的数目有限，而关键字实际上是无限的。
所以当两个关键字冲突时，我们要想办法解决冲突

方法一：分离链表法，我们将散列到同一个值得所有元素保存到一个表中

方法二：探测散列表，就是找空位置装入元素

方法三：双散列
"""

