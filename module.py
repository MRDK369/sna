def datagen():
    l=[]
    for i in range(1000):
        print("[] data gen")
        l.append(i)
    return l   

for i in datagen():
    print(i)