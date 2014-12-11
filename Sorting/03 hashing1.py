# lambda = num_of_items / table_size
# lambda is referred to as the 'load factor'
# e.g., if table_size is 11 and there are currently 6 items in table,
#       then the load factor lambda = 6/11

# Method 1 : Remainder Method
# key = item % table_size
def hash_by_remainder():
	print ""

# Method 2 : Folding Method
# Insert phone number: 436-555-4601
# (43,65, 55,46,01)
# 43+65+55+46+01 = 210
# key = 210 % table_size
def hash_by_folding():
	print ""

# Method 3 : Mid-Square Method
# Insert number 44
# Square the item 44**2 = 1936
# Take midsection 1936: 1'93'6
# key = 93 % table_size
def hash_by_midsquare():
	print ""

def hash_string(astring, table_size):
	sum = 0
	for ch in astring:
		sum = sum + ord(ch)
	return sum % table_size
print "\nhash_string('cat', 11) returns %d" % hash_string("cat", 11)

# Avoid collision of anagrams by using position+1 as scalar? sure, lets try it.
def hash_string_scalar(astring, table_size):
	sum = 0
	for ch in astring:
		sum = sum + ord(ch)*(astring.find(ch) + 1)
	return sum % table_size
print "\nhash_string_scalar('cat', 11) returns %d" % hash_string_scalar("cat", 11)


