import sys

def bubble_sort(li) :

    li.pop(0)
    for j in range(len(li) - 1) :
        
        for i in range( len(li) - 1) :
        
            if int(li[i]) > int(li[i+1]) :
            
                li[i],li[i+1] = li[i+1],li[i]
                 
    print(li)

li = sys.argv

bubble_sort(li)

