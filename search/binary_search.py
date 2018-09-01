def binarySearch(arr, item):
	
	first_index = 0
	last_index = len(arr)-1
	
	while first_index <= last_index:
	
		middle_index = (first_index+last_index)//2
	
		if arr[middle_index] ==  item:
			return ("record %d found at index %d" % (item, middle_index))
	
		else:
			if item > arr[middle_index]:
				first_index = middle_index + 1
			else:
				last_index = middle_index - 1
	return ("Element not found in the given array")



def binarySearchRecursion (arr, first_index, last_index, item):
	
	if last_index >= first_index:
		middle_index  = (first_index + last_index) // 2
		
		if arr[middle_index] == item:
			return ("record %d found" % middle_index)
		
		elif arr[middle_index] > item:
			return binarySearchRecursion(arr, first_index, middle_index-1, item)
		
		else:
			return binarySearchRecursion(arr, middle_index+1, last_index, item) 
    
    else:
		return 0
 

if __name__ == '__main__':
	
	print("Enter array element seperated by space")
	arr = list(map(int, input().split()))
	print("Enter element to find in an array")
	item = int(input())

	print (binarySearch(arr, item))
	print ("_____________________")
	
	first_index = 0
	last_index = len(arr)-1
	binary_search_result =  binarySearchRecursion(arr, first_index, last_index, item)

	if binary_search_result:
		print (binary_search_result)

	else:
		print ("Element not found in the given array")
	

