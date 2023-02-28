import sys

def ascii_sort(li) :

    li.pop(0)
    init_list = []
    ind = 0
    for word in li :

        wo = list(word)
        init_list.append(wo[0]) # Extract the first letter of each word an put it in list
        
    print(init_list)
    print("Base:",li)
    
    for j in range(len(init_list)) :
        
        mini_letter = init_list[ind]
        mini_word = li[ind]
        
        for i in range(ind, len(init_list)) : #Loop for searching the smallest ascii code of the initial list

            if ord(init_list[i]) < ord(mini_letter) :
                print(ind)
                print("Before :", i, mini_letter, mini_word)
                mini_letter = init_list[i]
                mini_word = li[i]
                print("After:", i, mini_letter, mini_word)
                
            if i == len(init_list) - 1 :
                
                    init_list.remove(mini_letter)
                    init_list.insert(ind, mini_letter)
                    
                    li.remove(mini_word)
                    li.insert(ind, mini_word)
                    print(init_list)
                    print(li)
                    
        ind+=1 #Agree to reduce the short range
        

li = sys.argv
ascii_sort(li)


        

        

        
