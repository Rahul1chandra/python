class Mydecorator:
	def __init__(self, function):
		self.f = function
	def __call__(self):
		return self.f()

@Mydecorator
def callingfunction():
	return ("calling_function !!!  ")

if __name__ == '__main__':
	print (callingfunction())