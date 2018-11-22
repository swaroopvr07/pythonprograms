def double(list):  
    if not list:
        return [];
    for c in list:
        finalList.append(2*c)
    
    return finalList;

list=[9,7,0]
finalList=[]
print (double(list))