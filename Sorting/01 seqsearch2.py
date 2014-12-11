def sequentialSearch(alist, item):
	pos = 0
	found = False

	for cur in alist:
		if cur == item:
			found = True

	return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))