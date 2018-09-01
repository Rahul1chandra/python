# Linear Search
# Search methodlogies:   

def linearsearch(arr_record, item):

	arr_length =  len(arr_record)
	for index in range(arr_length):
		if arr_record[index] ==  item:
			return ("record %d found at index %d" % (item, index))

	return ("Element not found")


def linearsearch_by_enumerate(arr_record, item):
	
	for index, value in enumerate(arr_record):
		if value == item:
			return ("record %d found at index %d" % (item, index))
	
	return ("Element not found")


def iterate_by_iter(arr_record, item):
	
	try:
		iter_object = iter(arr_record)
		index = 0
		while iter_object.__next__ :
			value = iter_object.__next__()
			if value == item:
				return ("record %d found at index %d" % (value, index))
			else:
				index += 1
		return ("Element not found")
	except StopIteration as obj_stopiteration:
		return ("Element not found")


if __name__ == '__main__':
	
	print("Enter array element seperated by space")
	arr = list(map(int, input().split()))
	print("Enter element to find in an array")
	item = int(input())
	print (linearsearch(arr, item))
	print ("_____________________")
	print (linearsearch_by_enumerate(arr, item))
	print ("_____________________")
	print (iterate_by_iter(arr, item))