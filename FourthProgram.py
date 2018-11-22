def write(filename,inputToWrite): 
   try:
    newFile=open(filename,mode="w")
    newFile.write(inputToWrite)
   except IOError:
    print("File not found or path is incorrect")
   finally:
    newFile.close()

filename="/Users/sudeepvr/Desktop/Test.txt"
inputToWrite="Hello"
print (write(filename,inputToWrite))