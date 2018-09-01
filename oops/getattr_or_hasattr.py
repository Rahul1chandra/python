# By using the function getattr, we can prevent exception, 
# if we provide a default value as the third argument

class Bank:

	def __init__(self, bank_id, bank_address, bank_type):
		self.bank_id = bank_id
		self.bank_address  = bank_address
		self.bank_type = bank_type

	def getBankType(self):
		return self.bank_type

	def getBankId(self):
		return self.bank_id


if __name__ == '__main__':
	bank_obj = Bank(1,"whitefield bangalore", "govt")

	############# get attribute ##################################
	print (getattr(bank_obj , 'bank_type', 'bank_type_not_found'))

	############ has attribute return the boolean value ###########
	print (hasattr(bank_obj , 'bank_type'))
	#> True
	print (hasattr(bank_obj , 'bank_locations'))
	# > False