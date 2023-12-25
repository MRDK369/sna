def create_adder(x):
    def adder(y):
        return(x+y)
    def subtractory(y):
        return(x-y)
    return adder, subtractory


add_5 , sub_5 = create_adder(40)
add_5 , sub_5 = create_adder(40)


l=[100,2,344,5,5,]
for v in l:
    print(add_5(v))
    print(sub_5(v))



print(list(map((lambda y: y+40),l)))
print(list(map(sub_5, l)))



print(list(filter((lambda x:x>1000),l)))