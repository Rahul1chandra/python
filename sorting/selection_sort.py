def selection_sort(arr):
	for upper_index in range(len(arr)):
		assume_min_index =  upper_index
		for inner_index in range(upper_index+1, len(arr)):
			if arr[assume_min_index] > arr[inner_index]:
				assume_min_index = inner_index
		arr[upper_index] , arr[assume_min_index] = arr[assume_min_index], arr[upper_index]
	return (arr)



if __name__ == '__main__':

	arr = [11, 23, -1121, 234, 0, 123, 1234]
	print ("before sorting ", arr)
	#arr = list(map(int, input().split()))
	print (selection_sort(arr))