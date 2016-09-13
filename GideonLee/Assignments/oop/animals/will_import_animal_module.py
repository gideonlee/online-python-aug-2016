from animal import Animal

animal = Animal('typical_animal')
animal.walk().walk().walk().run().run().displayHealth()

print '*****************'

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.name = name
		self.health = 150
	def pet(self):
		self.health += 5
		return self

my_dog = Dog('Peter Barker')
my_dog.walk().walk().walk().run().run().pet().displayHealth()

print '*****************'

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170
	def fly(self):
		self.health -= 10
		return self 
	def displayHealth(self):
		print 'this is a dragon!'
		super(Dragon, self).displayHealth()

toothless = Dragon('Toothless')
toothless.walk().walk().walk().run().run().fly().fly().displayHealth()
