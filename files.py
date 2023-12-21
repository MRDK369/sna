file_name = input("enter a filename :")
f = open(file_name, 'r')
print(f.read())
f.close()