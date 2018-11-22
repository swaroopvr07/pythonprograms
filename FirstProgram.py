list=[]

from sys import version_info

py3 = version_info[0] > 2 

if py3:
  string1 = input("Please enter first string: ")
  string2 = input("Please enter second string: ")
else:
  string1 = raw_input("Please enter first string: ")
  string2 = raw_input("Please enter second string: ")

def concatenate(string1, string2):  
     
   print ("First String: ", string1)
   print ("Second String: ", string2)
   for c in string1:
       if c not in list:
        list.append(c)
   for d in string2:
        if d not in list:
            list.append(d)
   str1 = ''.join(list)
   print str1       
   return str1;   


concatenate(string1 ,string2)