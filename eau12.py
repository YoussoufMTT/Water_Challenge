import sys
from UF import *

def diffmin(li) :
	
	mini = 100000
	step = 1
	for nb1 in range(1, len(li) - 1) :
		
		step += 1
		for nb2 in range(step, len(li)) :
			
				if  abs(int(li[nb1]) - int(li[nb2])) < mini :
				
					mini = abs(int(li[nb1]) - int(li[nb2]))
				
		
	print(abs(mini))
	
li = sys.argv
onlynum(li)

diffmin(li