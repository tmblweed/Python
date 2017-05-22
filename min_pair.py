#sort the arrays first 

a= [1,2,3,4,5,19]
b= [7,8,9,10,14,16,18]


def min_pair(arr1,arr2):

	idx_1,idx_2= 0,0
	min_diff = sys.maxint
	min_tuple=()

	while idx_1<len(arr1) and idx_2 < len(arr2):

		if abs(arr1[idx_1]-arr2[idx_2]) < min_diff:
			min_diff = abs(arr1[idx_1]-arr2[idx_2])
			min_tuple = (arr1[idx_1],arr2[idx_2])
		if arr1[idx_1] <= arr2[idx_2]:
			idx_1+=1
		else:
			idx_2+=1

	return min_tuple,


print min_pair(a,b)
