class Calc:
    #either function works
    '''
    #function1
    def add(self, a, b, c):
        return a+b+c
    '''
    #function2
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
            
c=Calc()
print(c.add(6,2,7))

