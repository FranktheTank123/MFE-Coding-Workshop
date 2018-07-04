# map
def add1(x):
	return x+1

input = [1,2,3]
output = [add1(x) for x in input]

output_v2 = list(map(add1, input)) # map is lazy


# reduce
from functools import reduce
def absmax(x,y):
	return max(abs(x),abs(y))

input = [1, 20, 3, 4, -11] 
output = reduce(absmax, input)

# filter
def is_gt_5(x):
	return x>5

input = [1,2,3,4,5,6,7]

output = list(filter(is_gt_5, input)) # [6,7], filter is also lazy


# more functionals!
# we can write any `add_n`:

def add_n(n):
	f = lambda x: x+n
	return f

add_2 = add_n(2)
add_2(3) # 5

# another way: 
def add(x,y):
	return x+y

add_2 = lambda x: add(x,2) # this is not elegant!

import toolz as t

@t.curry # this is equivalent to `partial`, but more elegant!
def add(x,y):
	return x+y

add_2_curry = add(2) # we only specify one value, meaning this is still a function
add_2_curry(3) # 5

# we usually do a lot of operations on a df
import pandas as pd

df = pd.DataFrame([
	['UCB', 100, 200_000],
	['CMU', 99, 150_000],
	['CU', 98, 160_000],
	['MIT', 30, None],
	['XXX', None, None],
], columns=['school_name', 'rank_score', 'salary'])


def drop_none(df):
	df = df.dropna(subset=['rank_score'])
	return df

def fill_salary(df):
	df['salary'] = df['salary'].fillna(100_000)
	return df

def cap_score(df):
	df['rank_score'] = df['rank_score'].where(df['rank_score']>50, 50)
	return df

cleaned_df = cap_score(fill_salary(drop_none(df)))

cleaned_df_v2 = t.pipe(
	df,
	drop_none,
	fill_salary,
	cap_score
)


