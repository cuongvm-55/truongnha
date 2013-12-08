def avgs(args=[]):
	'''
		Tính trung bình cộng của dãy tham số
	'''
	sum = 0.00
	num = 0.00
	for i in args:
		num = num + 1
		sum = sum + float(i)
	if num != 0:
		average = sum/num
		average	=	round(average, 1)
		return average
	else:
		return 0

def append_to_list( list_, *values):
	'''Adds `values` to the end of `list`.
	Example:
	| Append To List | ${L1} | xxx |   |   |
	| Append To List | ${L2} | x   | y | z |
	=>
	- ${L1} = ['a', 'xxx']
	- ${L2} = ['a', 'b', 'x', 'y', 'z']
	'''
	for value in values:
		list_.append(value)
			
def combine_lists(*lists):
	'''Combines the given `lists` together and returns the result.

	The given lists are not altered by this keyword.

	Example:
	| ${x} = | Combine List | ${L1} | ${L2} |       |
	| ${y} = | Combine List | ${L1} | ${L2} | ${L1} |
	=>
	- ${x} = ['a', 'a', 'b']
	- ${y} = ['a', 'a', 'b', 'a']
	- ${L1} and ${L2} are not changed.
	'''
	ret = []
	for item in lists:
		ret.extend(item)
	return ret

def	add(arg1, arg2):
	num1 = float(arg1)
	num2 = float(arg2)
	return	(num1+num2)
