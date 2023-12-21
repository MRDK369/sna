f= open("demofile.txt" , "a")
f.write("\nsee you bye")
f.close()



f= open("demofile.txt", "r")
print(f.read())