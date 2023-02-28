import sys
from UF import onenum

def fibonacci(ind):
	
	for i in range(2, ind+1) :
		
		elem = fibo[i-1] + fibo[i-2]
		fibo.append(elem)
		
	print(fibo[ind])

ind = int(sys.argv[1])
fibo = [0,1]

onenum(sys.argv)

if ind < 1 :
	
	print -1
	exit()

	
fibonacci(ind)