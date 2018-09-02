def decoratorFunction(arg_function):
	
	def modifyFunction(arg_function_Args):
		"""mofify the functions behaviour as per needed 
		"""
		return arg_function(arg_function_Args)

	return modifyFunction



@decoratorFunction
def mainfunction(arg):
	return ("%s is an argument " % arg)


if __name__ == '__main__':
	arg = input("Enter an string argument  ")
	print (mainfunction(arg))