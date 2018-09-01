class Myclass:
	pass

if __name__ == '__main__':
	obj_myclass_1 = Myclass()
	obj_myclass_2 = Myclass()

	
	# 1)  ##########  operations ############
	print (bool(obj_myclass_1 == obj_myclass_2))
	# > False

	
	# 2)  ######## Class Attribute #############
	obj_myclass_1.name = "python class"
	print (obj_myclass_1.name)
	# > python class
	
	
	# 3)  ####### Class Attributes as the dict ##
	print (obj_myclass_1.__dict__)
	# > {'name': 'python class'}
	print (obj_myclass_2.__dict__)
	# > {}
	