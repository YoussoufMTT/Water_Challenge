import sys

def ascii_sort(lst) :

    lst.pop(0)
    wrd =[]
    lng = len(lst)
    
    for word in lst :
        
        wrd.append(list(word))
    
    for j in range(lng - 1) :
        
        #mini_letter = wrd[ind][0]
        #mini_word = lst[ind]
        
        for i in range(lng - 1) : #Loop for searching the smallest ascii code of the initial list

            if wrd[i][0] > wrd[i+1][0] :
                
                wrd[i][0], wrd[i+1][0] = wrd[i+1][0], wrd[i][0]
                lst[i], lst[i+1] = lst[i+1], lst[i]
                

            elif wrd[i][0] == wrd[i+1][0] :

                idx = 0

                while wrd[i][idx] == wrd[i+1][idx] : # If the first letter are the same

                    idx+=1
                    
                wrd[i][0], wrd[i+1][0] = wrd[i+1][0], wrd[i][0]
                lst[i], lst[i+1] = lst[i+1], lst[i]

                    
    print(lst)                        

li = sys.argv
ascii_sort(li)


        

        

        
