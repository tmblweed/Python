

def group_anagram(list):
""" Takes a list, creates a dictionay of  sorted value to variants of the value, then 
iterates over the dictionary values and appends them to a list in order"""

	result_dict = {}
	result_sorted = []

	for i,v in enumerate(a):
		key = "".join(sorted(v))
		if key not in result_dict:
			result_dict[key]=[v]
		else:
			result_dict[key].append(v)

	for value in result_dict.values():
		result_sorted +=[sorted(value)]
	return result_sorted

print group_anagram(['cat','bat','mit','tac','tab'])
#[['bat', 'tab'], ['mit'], ['cat', 'tac']]
