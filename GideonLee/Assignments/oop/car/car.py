class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
	def display_all(self):
		print 'Price: {} | Speed: {} | Fuel: {} \nMileage: {} | Tax: {}'.format(self.price, self.speed, self.fuel, self.mileage, self.tax)

cars = []
bmw = Car(50000, 160, '50%', 300)
audi = Car(55000, 150, '75%', 25)
mercedes = Car(15000, 155, '100%', 70000)
toyota = Car (3000, 110, '5%', 120000)
honda = Car(9000, 125, '35%', 70000)

cars.append(bmw)
cars.append(audi)
cars.append(mercedes)
cars.append(toyota)
cars.append(honda)

for car in cars:
	car.display_all()
	print '_____________________________________'
