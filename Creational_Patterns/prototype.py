# prototype

import copy

class Prototype:
	def __init__(self):
		self._objects = {}

	def register_object(self,name,obj):
		self._objects[name] = obj

	def unregister_object(self,name):
		if name in self._objects:
			del self._objects[name]

	def clone(self,name,attr):
		obj = copy.deepcopy(self._objects[name])
		obj.__dict__.update(attr)
		return obj

class Car:
	def __init__(self):
		self.name = 'Benz'
		self.color = 'red'
		self.options = 'Ex'
	def __str__(self):
		return '{}|{}|{}'.format(self.name,self.color,self.options)

c = Car()
portotype = Prototype()
portotype.register_object('car',c)
newCar = portotype.clone('car',{'name':'Audi'})
print(newCar)