# no more pointer, refernce and value passing in Python!

def f(a, b):
	a += b
	return a

x = 1
y = 2
f(x, y) # 3
x, y # 1, 2 


a = [1, 2]
b = [3, 4]
f(a, b) # [1, 2, 3, 4]
a, b # ([1, 2, 3, 4], [3, 4]) --> why?

t = (10, 20)
u = (30, 40)
f(t, u) # (10, 20, 30, 40)
t, u # ((10, 20), (30, 40)) --> why?


def g(a, b):
	print(id(a))
	a += b
	print(id(a)) # id will change if a is immutable

g(x,y)
g(a,b)
g(t,u)