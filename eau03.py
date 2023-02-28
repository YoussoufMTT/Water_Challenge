import sys

def reverse_arg(li) :
	
	
	for ind in range(len(li) - 1, 0, -1 ):
		
		print(li[ind])
		
		
		
reverse_arg(sys.argv)