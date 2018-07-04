def identity(x):
	return x

def divide2(x):
	return x//2 # a bug! we actually want x/2

def multiply2(x):
	return x*2

x = 5.
y = identity(multiply2(divide2(x)))
print(y) # this gives 4 instead of 5!

# Q: Imagine each function is really long, and we want to debug what's going on.
# One way is to print the results of the output of each function:

def identity(x):
	out = x
	print(f'Function identity input {x}, output {out}')
	return out

def divide2(x):
	out = x//2
	print(f'Function divide2 input {x}, output {out}')
	return out

def multiply2(x):
	out = x * 2
	print(f'Function multiply2 input {x}, output {out}')
	return out

y = identity(multiply2(divide2(x)))
print(y)

# this is okay, but too much.
# try decorators!
# they are functional (function in, function out)

def print_decorator(f):
	def wrapper(*args, **kwargs):
		res = f(*args, **kwargs)
		print(f'Function Name: {f.__name__}, Input: args:{args} kwargs:{kwargs}, return: {res}')
		return res
	return wrapper

@print_decorator
def identity(x):
	return x

@print_decorator
def divide2(x):
	return x//2 # a bug! we actually want x/2

@print_decorator
def multiply2(x):
	return x*2

y = identity(multiply2(divide2(x)))
print(y)

# some useful decorators to keep in mind:
# - check if an input df has no NAs
# - check if an input df has certain columns
# - time the function
# ...
