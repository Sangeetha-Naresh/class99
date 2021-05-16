import os

#os.system("date")

#os.mkdir("D:\whitehatclasses\AI and ML\class99\sample")
#print(os.getcwd())

#path="D:\whitehatclasses\AI and ML\class99\sample\ file1.txt" #remember to give a space before file1
path="D:/whitehatclasses/AI and ML/class99/san"
#value=os.path.exists(path)
#print(value)

''' root_ext=os.path.splitext(path)
print(root_ext)
print(type(root_ext)) # returns tuple
print("the root is: "+ root_ext[0])
print("the extension of the file is: "+ root_ext[1]) '''

print(os.listdir(path))