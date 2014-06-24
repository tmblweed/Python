

with open ('line_length.txt', 'r') as data_file:
	input_file = data_file.read().splitlines()

numbers_to_print = int(input_file[0])

sorted_input_file = sorted(input_file, key=len, reverse=True)

for data in sorted_input_file[:numbers_to_print]:
		print data