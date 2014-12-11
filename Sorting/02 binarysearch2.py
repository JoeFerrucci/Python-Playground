def binarySearch(alist, item):
	if len(alist) == 0:
		return False
	else:
		mid = len(alist) / 2
		if alist[mid] == item:
			return True
		else:
			if item < alist[mid]:
				return binarySearch(alist[:mid], item)
			else:
				return binarySearch(alist[mid+1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))