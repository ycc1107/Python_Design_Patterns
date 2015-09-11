# Proxy
# postpone object creation unless absolutely necessary
import time
class Producer:
	def produce(self):
		print('producer is working harding')

	def meet(self):
		print('producer has time to meet you now')

class Proxy:
	def __init__(self):
		self.occupied  = 'No'
		self.producer = None

	def produce(self):
		print('artist checking if producer is available...')
		if self.occupied == 'No':
			self.producer = Producer()
			time.sleep(2)
			self.producer.meet()
		else:
			time.sleep(2)
			print('producer is busy')

proxy = Proxy()
proxy.produce()
proxy.occupied = 'Yes'
proxy.produce()