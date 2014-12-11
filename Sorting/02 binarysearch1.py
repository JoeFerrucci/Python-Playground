def binarySearch(alist, item):
	low = 0
	high = len(alist) - 1
	found = False

	while low <= high and not found:
		# use // in Py3 for int division
		mid = (low + high) / 2

		if alist[mid] == item:
			found = True
		else:
			if item < alist[mid]:
				high = mid - 1
			else:
				low = mid + 1

	return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))