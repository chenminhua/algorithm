q_sort = lambda l : l if len(l) <= 1 else q_sort([x for x in l[1:] if x < l[0]]) + [l[0]] + q_sort([x for x in l[1:] if x > l[0]])

import random

a = [random.random() for i in range(40)]
print q_sort(a)