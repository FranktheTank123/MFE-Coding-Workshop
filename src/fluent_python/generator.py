# Q: imagine we have a giant wikipedia.txt on our hard drive, 
# and we want to get some summary out of it (e.g., word count), 
# what should we do?

with open('data/wikipedia_sample.txt', 'r') as f:
	print(f.readline())
	print(f.readline())
	print(f.readline())
	print(f.readline())


# Q: can we write a generator
# e.g., all even nubmers up to n:
n = 100
even_numbers = (x for x in range(n+1) if not x%2)

print(next(even_numbers))  # need `next` to trigger an evaluation, which is lazy.


def even_number_generator(n):
	if n < 1:  # edge case
		yield None
	
	for i in range(1, n+1):
		if i % 2 == 0:
			yield i

even_numbers = even_number_generator(n)

print(next(even_numbers))
# len(even_numbers) # this would fail! cannot `len` a generator.

def another_even_number_generator_bad(n):
	yield even_number_generator(n) # wrong way!

even_numbers = another_even_number_generator_bad(n)
print(f'This is bad, which will NOT work: {next(even_numbers)}')


def another_even_number_generator_good(n):
	yield from even_number_generator(n) # need to yield from another generator, think of arg vs *args

even_numbers = another_even_number_generator_good(n)
print(f'This is good, which will work: {next(even_numbers)}')


