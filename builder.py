# builder
# director 
# abstract builder: interfaces
# concrete builder
# product
class Director():
	def __init__(self,builder):
		self._builder = builder

	def construct_car(self):
		self._builder.create_new_car()
		self._builder.add_model()
		self._builder.add_tires()
		self._builder.add_engine()

	def get_car(self):
		return self._builder.car

class Builder():
	def __init(self):
		self.car = None
	def create_new_car(self):
		self.car = Car()

class Car():
	def __init__(self):
		self.model = None
		self.tires = None
		self.engine = None
	def __str__(self):
		return '{}|{}|{}'.format(self.model, self.tires, self.engine)

class ConcreteBuilder(Builder):
	def add_model(self):
		self.car.model = 'GLK350'
	def add_tires(self):
		self.car.tires = 'regular'
	def add_engine(self):
		self.car.engine = 'AMG'


builder = ConcreteBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)


	


