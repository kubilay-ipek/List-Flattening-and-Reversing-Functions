list = [[1, 2], [3, 4], [5, 6, 7]]   # a given list containing other lists inside.

def rev(x):                ##  defining the reversing function.
   
    for i in x:            ## for each element of given list (x)
        
        if isinstance (i, type(list)):   #checking the type of current iteration, if it's a list, put it back in the function.
                                        
            rev(i)
    
    x.sort(reverse = True)  ##the code for reversing the object.
            
        
    return list          ##calling back the list.
    
    
    www.patika.dev
