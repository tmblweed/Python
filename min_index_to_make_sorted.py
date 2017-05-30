#return the indexes of element you need to sort to make a partially sorted array sorted
a = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
b=[0, 1, 15, 25, 6, 7, 30, 40, 50]  #2,5

n = len(a)-1

def minimumUnsorted(a):

	for idx in range(len(a)-1):
		if a[idx] > a[idx+1]:
			s = idx
			break
	for idx in reversed(range(len(a)-1)):
		if a[idx]<a[idx-1]:
			e = idx
			break
	max_val= max(a[s:e+1])
	min_val =min(a[s:e+1])

	for idx in range(len(a[0:s])):
		if a[idx] > min_val:
			min_val=a[idx]
			s = idx
			break

	for i in range(len(a)-1,e,-1):
		if(a[i] < max_val):
			e = i
			break


minimumUnsorted(b)
