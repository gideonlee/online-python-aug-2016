
class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print 'Price: {}'.format(self.price)
		print 'Maximum Speed: {}'.format(self.max_speed)
		print 'Total Mileage: {}'.format(self.miles)
	def ride(self):
		print 'Riding'
		self.miles += 10
	def reverse(self):
		print 'Reversing'
		if self.miles > 0:
			self.miles -= 5

ducati = Bike(10000, '145mph')
harley_davidson = Bike(13000, '100mph')
kawasaki = Bike(5000, '120mph')

# Have the first instance ride three times and reverse
for i in range(3):
	ducati.ride()
ducati.reverse()
ducati.displayInfo()

# Have the second instance ride two times and reverse two times
for i in range(2):
	harley_davidson.ride()
for i in range(2):
	harley_davidson.reverse()
harley_davidson.displayInfo()

# Have the third instance reverse three times
for i in range(3):
	kawasaki.reverse()
kawasaki.displayInfo()