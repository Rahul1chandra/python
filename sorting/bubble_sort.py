def bubble_sort(arr):
	for i in range(len(arr)):
		for j in range(0, len(arr)-1 -i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr


if __name__ == '__main__':
	print ("Enter the element of the array")
	arr = list(map(int, input().split()))
	print ("The array before sort  :", end='' )
	print (arr)
	print ("The array after sort : ",bubble_sort(arr))	