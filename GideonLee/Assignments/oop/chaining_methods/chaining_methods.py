class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print 'Price: {}'.format(self.price)
		print 'Maximum Speed: {}'.format(self.max_speed)
		print 'Miles: {}'.format(self.miles)
		return self
	def ride(self):
		print 'Riding'
		self.miles += 10
		return self 
	def reverse(self):
		print 'Reversing'
		if self.miles > 0:
			self.miles -= 5
		return self

ducati = Bike(1000, '145mph')
kawasaki = Bike(5000, '120mph')

print 'Ducati: ...'
ducati.ride().ride().ride().reverse().reverse().reverse().ride().ride().displayInfo()

print '______________\n'
print 'Kawasaki: ...'
kawasaki.ride().reverse().reverse().reverse().ride().reverse().displayInfo()