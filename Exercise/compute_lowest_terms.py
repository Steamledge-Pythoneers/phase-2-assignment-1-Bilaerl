## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	#convert the given string into two integers
	num, denom = string_to_nums(x)

	if denom == 0:
		return 'Undefined'
	elif num == 0:
		return '0'
	else:
		#get the highest possible common multiple of the two numbers
		hpcf = highest_possible_common_factor(num, denom)

		if hpcf < 0:
			#when the numerator or both terms are negative
			for n in range(hpcf, 0):
				if (num % n == 0) and (denom % n == 0):
					num = num // n
					denom = denom // n
					break
		else:
			#when both terms are possitive
			for n in reversed(range(1,hpcf+1)):
				if (num % n == 0) and (denom % n == 0):
					num = num // n
					denom = denom // n
					break
		
		if denom < 0:
			#when denominator is negative
			num, denom = -num, -denom
		
		#convert terms from integers to string
		result = nums_to_string(num, denom)
		return result


def string_to_nums(string):
	"""Convert given fraction from string into integers

	INPUT:
	string (str) - Fraction in string form

	OUTPUT:
	splitted_nums (list) - A list consisting of two integers representing the numerator and denominator of given fraction respectively
	"""

	#split string
	splitted_strings = string.split('/')
	#convert splitted strings to integers
	splitted_nums = [int(string) for string in splitted_strings]

	return splitted_nums


def nums_to_string(num, denom):
	"""Convert given integers into a fraction in string form

	INPUT:
	num (int) - The numerator of the fraction
	denom (int) - Denominator of the fraction

	OUTPUT:
	string (str) - fraction in string form
	"""

	string = str(num) +'/'+ str(denom)
	return string


def highest_possible_common_factor(num, denom):
	""" Find the highest possible common factor between two numbers

	The highest possible common factor of given set of numbers is a number that might or might not be
	the Highest Common Factor of those numbers, but above which the given numbers has no common factor

	INPUT:
	num (int) - The first number
	denom (int) - The second number

	OUTPUT:
	(int) - The highest possible common factor of the two given numbers
	"""

	#find the smallest between num and denom
	smallest = min(abs(num), abs(denom))
	
	#find the highest possible common factor
	return smallest if (num % smallest == 0) and (denom % smallest == 0) else smallest // 2
	

if __name__ == "__main__":
	print(lowest_terms('1/1'))