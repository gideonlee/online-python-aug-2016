# Part 1
# Create a python class that allows for add and subtract that accepts at least 1 parameter
class MathDojo1(object):
	def __init__(self):
		self.total = 0
	def add(self, *x):
		for i in x:
			self.total += i 
		return self
	def subtract(self, *x):
		for i in x:
			self.total -= i
		return self
	def result(self):
		print 'Total: ' + str(self.total)

md = MathDojo1().add(2).add(2, 5).subtract(3, 2).result()

# Part 2
# Refactor it to allow the user to input at least one integer(s) and/or list(s) as a parameter with any number 
# values passed into the list
class MathDojo2(object):
	def __init__(self):
		self.total = 0
	def add(self, *x):
		# Search through the length of the given numbers
		for i in range(len(x)):
			# If it's a list ...
			if type(x[i]) == list:
				for j in range(0, len(x[i])):
					self.total += x[i][j]
			# Else if it's just a float or an int
			else:
				self.total += x[i]
		return self
	def subtract(self, *x):
		for i in range(len(x)):
			if type(x[i]) == list:
				for j in range(len(x[i])):
					self.total -= x[i][j]
			else:
				self.total -= x[i]
		return self
	def result(self):
		print 'Total is: ' + str(self.total)

cd = MathDojo2().add([1], 3, 4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3]).result()

# Part 3
# Make any needed changes in MathDojo in order to support tuples of values in addition to lists and singletons
class MathDojo3(object):
	def __init__(self):
		self.total = 0
	def add(self, *x):
		for i in range(len(x)):
			# Exactly like Part 2 except with this added tuple conditional 
			if type(x[i]) == list or type(x[i]) == tuple:
				for j in range(0, len(x[i])):
					self.total += x[i][j]
			else:
				self.total += x[i]
		return self
	def subtract(self, *x):
		for i in range(len(x)):
			if type(x[i]) == list or type(x[i]) == tuple:
				for j in range(len(x[i])):
					self.total -= x[i][j]
			else:
				self.total -= x[i]
		return self
	def result(self):
		print 'Total is: ' + str(self.total)

bd = MathDojo3().add([1], (2, 3)).subtract([1.25, 3.75]).add(2).subtract([1]).result()