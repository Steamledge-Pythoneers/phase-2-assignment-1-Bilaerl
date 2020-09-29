## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	num, denom = string_to_nums(x)

	if num == 0:
		return '0'
	else:
		num, denom = find_lowest_terms(num,denom)
		result = nums_to_string(num,denom)
		return result


def find_lowest_terms(num,denom):
	hpcf = highest_possible_common_factor(num,denom)

	if hpcf < 0:
		for n in range(hpcf, 0):
			if (num % n == 0) and (denom % n == 0):
				num = num // n
				denom = denom // n
				break
	else:
		for n in reversed(range(1,hpcf+1)):
			if (num % n == 0) and (denom % n == 0):
				num = num // n
				denom = denom // n
				break
	
	return num, denom


def string_to_nums(string):
	splitted_strings = string.split('/')
	splitted_nums = [int(string) for string in splitted_strings]
	return splitted_nums


def nums_to_string(num,denom):
	string = str(num) +'/'+ str(denom)
	return string


def highest_possible_common_factor(num,denom):
	#find the smallest between num and denom
	smallest = num if abs(num) < abs(denom) else denom
	
	if (num % smallest == 0) and (denom % smallest == 0):
		hpcf = smallest 
	elif smallest == 1:
		hpcf = 1
	elif smallest == 2:
		hpcf = 2
	elif smallest == 3:
		hpcf = 3
	else:
		hpcf = smallest//2

	#return highest possible common factor
	return hpcf


if __name__ == "__main__":
	print(lowest_terms('20/10'))