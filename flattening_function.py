mylist = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flattened_list = []       ## an empty list to put the flattened objects in. ##
def flattener(x):      
        for i in x:                        ## loop.  
            if isinstance(i,type(list)):   ## Checking the type of the object. if it's a list, put it back into the loop. 
                flattener(i)
            else:                          ##  if not, just add it to the flattened_list as it is, regardless of whether it is an int, str, etc.
                flattened_list.append(i)
flattener(mylist)                          ## to run the function for the given list at the top. Not necessary since you could call it by using the function flattener.
print(flattened_list)                      ## printing the results.



www.patika.dev
            
