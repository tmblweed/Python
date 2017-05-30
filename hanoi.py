def hanoi(stack_size,from_stack,target_stack,spare_stack):
	if stack_size==1:
		print "move from " + from_stack + " to " + target_stack
	else:
		hanoi(stack_size-1,from_stack,spare_stack,target_stack)
		hanoi(1,from_stack,target_stack,spare_stack)
		hanoi(stack_size-1,spare_stack,target_stack,from_stack)

print hanoi(3,"A","B","C")
