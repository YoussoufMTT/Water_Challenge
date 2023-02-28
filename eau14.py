import sys

def select_sort(li) :
    
    li.pop(0)
    ind = 0
    
    for j in range (len(li)) :
        
            mini = li[ind]
            
            for i in range(ind, len(li)) : # Reduce the sort of range with ind increasing
                
                if  int(li[i]) < int(mini) :
                    
                    mini = li[i]

                if i  == len(li) - 1 : 
                    
                    li.remove(mini)
                    li.insert(ind , mini) # Insert the elements in ascending order
                  
                
            ind+=1
    print(li)
    
li = sys.argv
select_sort(li)
