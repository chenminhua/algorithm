print max([1,3,4])  #4
print min([1,2,3])  #1

#count
a = [1,2,3,3,2,1,3,3]
print a.count(3)   #4

#extend
a = [1,2,3]
a.extend([1,2,3])
print a  #[1, 2, 3, 1, 2, 3]
print [1,2,3] + [1,2,3]  #[1, 2, 3, 1, 2, 3]

#index
a = [1,23,3,32]
print a.index(23)  #1 

#insert
a.insert(0,33) #[33,1,23,3,32]
print a

#remove
a.remove(32)
print a        #[33,1,23,3]

#sort
a.sort()
print a
b = [33,24,65,28,243]
b.sort(reverse=True)
print b

#reverse
b.reverse()
print b