a = [	['a','b','c','d'],
		['n','o','p','e'],
		['m','t','q','f'],
		['l','s','r','g'],
		['k','j','i','h']
]

# order of operatoins = right, down,left,up

m_x=len(a[0])-1
m_y=len(a)-1
new = []
minimum = [0,0]
maximum= [m_x,m_y]
cursor = [0,0]
state = 'right'
count  = 0



print 'MaxX: ' + str(m_x) + ' MaxY: ' + str(m_y)


#while minimum != maximum:
while minimum[0] <= maximum[0] and minimum[1] <= maximum[1]:
	#print str(cursor) + ' ' + str(minimum) + ' ' + str(maximum)  + state
	print a[cursor[1]][cursor[0]]
	count+=1
	if state == 'right':
		cursor[0]=cursor[0]+1 			# x = x + 1
		if cursor[0] == maximum[0]:		# cursor.x == maximum.x
			state = 'down'
			minimum[1]=minimum[1]+1 	# minimum.y ++
		continue
	if state == 'down':
		cursor[1]=cursor[1]+1 			# y = y + 1
 		if cursor[1] == maximum[1]:		# cursor.y == maximum.y
			state = 'left'
			maximum[0]=maximum[0]-1 	# maximum.x --
		continue
	if state == 'left':
		cursor[0]=cursor[0]-1 			# x = x - 1
		if cursor[0] == minimum[0]:		# cursor.x == minimum.x
			state = 'up'
			maximum[1]=maximum[1]-1 	# maximum.y --
		continue
	if state == 'up':
		cursor[1]=cursor[1]-1 			# y = y - 1
 		if cursor[1] == minimum[1]:		# cursor.y == minimum.y
			state = 'right'
			minimum[0]=minimum[0]+1 	# minimum.x ++
		continue
print a[cursor[1]][cursor[0]]
