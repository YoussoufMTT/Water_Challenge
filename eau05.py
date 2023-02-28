import sys

from UF import onenum

def fromfirst(nb) :
	
	if nb == 1 : 
		print("1 not accepted.")
		exit()
		
	for k in range(2, nb) :
			
		if nb % k == 0 :
			print(nb," is not a prime number.")
			nb+=1
	print (nb," is a prime number.")
	
			
nb = int(sys.argv[1])			
onenum(sys.argv)

fromfirst(nb)
