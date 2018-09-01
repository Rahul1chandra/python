# Definitations 
# Data Abstraction = Data Encapsulation + Data Hiding 

# Encapsulation is seen as the bundling of data with the methods that operate on that data

# Information hiding on the other hand is the principle that some internal information or 
# data is "hidden", so that it can't be accidentally changed


#####################################################################################################

# Public

# name	
# These attributes can be freely used inside or outside of a class definition.



# Protected

# _name	
# Protected attributes should not be used outside of the class definition, unless inside of a subclass definition. 



# Private

# __name	
# This kind of attribute is inaccessible and invisible. 
# It's neither possible to read nor write to those attributes,
# except inside of the class definition itself.
##########################################################################################################

##########################################################################################################

##########################################################################################################
class AccessAttributeClass:
    
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"


if __name__ == '__main__':
	classA_obj= AccessAttributeClass()

	## public attribute #######################################
	print ( hasattr(classA_obj, 'pub') )
	#> True

	##  protected attribute ###################################
	print (hasattr(classA_obj, '_prot'))
	#> True

	##  private  attribute is not accessable  ##################
	print (hasattr(classA_obj, '__priv'))

	try:
		print (classA_obj.__priv)
	except AttributeError as err:
		print ("Error:: %s " % str(err))
