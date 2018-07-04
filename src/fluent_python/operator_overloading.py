class Boo:
	def __init__(self):
		self.x = 'boo'

	def __add__(self, right):
		return self.x + str(right)

boo = Boo()
print(boo + 3)  # ‘boo3’
# print(3 + boo)  # error!

class Boo:
	def __init__(self):
		self.x = 'boo'
	def __add__(self, right):
		return self.x + str(right)
	def __radd__(self, left):
		return str(left) + self.x

boo = Boo()
print(3 + boo)  # now it works! 
# Q: why not using 3's `__add__`? what's the resolve order?


# how about len()?
class Boo:
	def __len__(self):
		return 1000

boo = Boo()
print(len(boo))

# about boo[...]
class Boo:
	def __init__(self):
		self.x = 'boo'
	def __getitem__(self, key):
		return self.x + str(key)  # abuse again!

boo = Boo()
print(boo['foo'])