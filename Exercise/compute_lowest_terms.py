## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	return ""

def string_to_nums(string):
	splitted_strings = string.split('/')
	splitted_nums = [int(string) for string in splitted_strings]
	return splitted_nums

if __name__ == "__main__":
	num, denom = string_to_nums('2/3')
	print(num)
	print(denom)
	print (num + denom)