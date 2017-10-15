############## Decorator Example ##################

#### Example 1st #### 

from functools import wraps
def a_new_decorator(a_func):
	
	def wrapTheFunction():
		print("Inside my Wrapper functions")
		a_func()

	return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
	"""
		*********************   This is my decorator doc        ************* 
	"""
	print("I am the function which needs some decoration to remove my foul smell")
	
a_function_requiring_decoration()    



###### Example 2nd #######

########## Make Uppercase #################
_string = "letter in lowercase"

def makeUpper(_str):
	
	def wrapper():
		if not _string.upper():
			print _string.lower()
		else:
			print _string.upper()

	return wrapper	

print ("before decorator:: %s" % _string )

@makeUpper
def myFunction():
	pass

myFunction()

