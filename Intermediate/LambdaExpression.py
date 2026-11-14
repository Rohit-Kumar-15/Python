#lambda Expression

add10 = lambda x: x+10

def add10func(x):
    return x+10

mult = lambda x,y: x*y

point2D = [(1,2), (15,1), (5,-1), (10,4)]
point2D = sorted(point2D, key = lambda x: x[1])
point2D = sorted(point2D, key = lambda x: x[0]+x[1])

#map(func, sequence)
a = [1,2,3,4,5]
b=map(lambda x: x*2, a)
print(list(b))

c = [x*2 for x in a]
print(c)

#filter(func, seq)
print (filter(lambda x: x%2 == 0, a))
d = [x for x in a if x%2 ==0]
print ()

#reduce(func, seq)
from functools import reduce
print(reduce(lambda x,y: x*y , a))  #reduce list into single element