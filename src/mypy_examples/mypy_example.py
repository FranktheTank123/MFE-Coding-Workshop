from typing import List

def add_int(x: int, y: int) -> int:
	return x + y

add_int(1, 2)
add_int(1., 2.) # mypy error!


def print_decorator(f):
	def wrapper(*args, **kwargs):
		res = f(*args, **kwargs)
		print(f'Function Name: {f.__name__}, Input: args:{args} kwargs:{kwargs}, return: {res}')
		return res
	return wrapper


class UCBMFE:
	def __init__(self, name):
		self.name = name

	def __str__(self):  # for print
		return f'UCBMFE: {self.name}'

	def __repr__(self):  # for print in List
		return self.__str__()

	@property	
	def getGPA(self):
		return 4.0

class CMUMFE:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return f'CMUMFE: {self.name}'

	@property	
	def getGPA(self):
		return 3.9

@print_decorator
def calc_mean_GPA(students: List[UCBMFE]) -> float:
	if not len(students):
		return 0.

	gpas = [student.getGPA for student in students]
	return sum(gpas) / len(gpas)

names = ['A', 'B', 'C']

students_good = [UCBMFE(name) for name in names]

calc_mean_GPA(students_good) # no problem

calc_mean_GPA(students_good + [CMUMFE("What's up")])  # python will run, but mypy complains