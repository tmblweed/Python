# import sys
# from collections import Counter
# from collections import defaultdict
# from collections import OrderedDict



with open ('line_length.txt', 'r') as data_file:
	input_file = data_file.read().splitlines()


numbers_to_print = int(input_file[0])



sorted_input_file = sorted(input_file, key=len, reverse=True)

print sorted_input_file

for data in sorted_input_file[:numbers_to_print]:
		print data






# numbers_to_print = int(input_file[0])
# print " The %i longest lines are as follows"  %(numbers_to_print)
# input_file.pop(0)
# # print input_file

# new_data = defaultdict(list)
# newer_data = defaultdict(list)
	
# print ""
# length = 0

# for data in input_file:
# 	data.replace('\n', ' ')
# 	length = len(data)
# 	# new_data[data].append(len(data))
# 	new_data[length].append(data)


# # for i in range(numbers_to_print):
# # 	print newer_data
# #newer_data = sorted(new_data)



# for key in sorted(new_data):

#     print "%s: %s" % (key, new_data[key])


# # for i in range(numbers_to_print)


# # for key in sorted(new_data):

# #     print "%s: %s" % (key, new_data[key])


# # print main_dict

# # main_dict = dict((data,input_file.count(data)) for data in input_file)
# # print main_dict



# # count = 0
# # for data in input_file:
# # 	# numbers = Counter(data)
# # 	# print numbers
# # 	count = count + 1
# # 	print count


# # print numbers