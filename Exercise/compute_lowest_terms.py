## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	num, denom = string_to_nums(x)
	hpcf = highest_possible_common_factor(num,denom)

	print(f'Num: {num}')
	print(f'Denom: {denom}')
	print(f'HPCF: {hpcf}')

	for n in reversed(range(1,hpcf+1)):
		if (num % n == 0) and (denom % n == 0):
			num = num // n
			denom = denom // n
			break

	print(f'lowest num is {num} and lowest denom is {denom}')

	#return ""


def string_to_nums(string):
	splitted_strings = string.split('/')
	splitted_nums = [int(string) for string in splitted_strings]
	return splitted_nums


def highest_possible_common_factor(num,denom):
	#find the smallest between num and denom
	smallest = abs(num) if abs(num) < abs(denom) else abs(denom)
	
	if smallest == 1:
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
	lowest_terms('15/12')