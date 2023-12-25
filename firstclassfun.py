def create_adder(x):
    def adder(y):
        return(x+y)
    def subtractory(y):
        return(x-y)
    return adder, subtractory


add_5 , sub_5 = create_adder(40)
print(add_5(100))
print(sub_5())