class Employee:
	
	def __init__(self, name, phn):
		self.name = name
		self.phn = phn

	def __str__(self):
		"""string representations of class Name Employee
		"""
		return "%s -%d" % (self.name, self.phn)

class Department(Employee):

	def __init__(self, name, phn, dept_name):
		Employee.__init__(self, name, phn)
		self.dept_name = dept_name


get_name = input("Enter the name")
get_phone_no  = int(input("Enter the employee phone no:"))

emp_obj = Employee(get_name, get_phone_no)
print (emp_obj)