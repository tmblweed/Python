
def isShuffle(str1,str2,str3):
	if len(str1)+len(str2)!=len(str3):
		return False	
	if not str1 or not str2 or not str3:
		if str1+str2==str3:
			return True
		else:
			return False
	if str1[0]!=str3[0] and str2[0]!=str3[0]:
		return False
 
	if str1[0]==str3[0] and isShuffle(str1[1:],str2,str3[1:]):
		return True
	if str2[0]==str3[0] and isShuffle(str1,str2[1:],str3[1:]):
		return True

	return False

print isShuffle('abc','def','dabecf')
