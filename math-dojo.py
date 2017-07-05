from types import *

# Part I
class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, x, *args):
        self.result += x
        if args:
            for num in args:
                self.result += num
        return self

    def subtract(self, x, *args):
        self.result -= x
        if args:
            for num in args:
                self.result -= num
        return self

md = MathDojo().add(2).add(2, 5).subtract(3, 2).result
print md



print "-" * 50




# Part II
class MathDojo(object):
    def __init__(self):
        self.result = 0

    def recur(self, lst):
        sum = 0
        if type(lst) == ListType:
            for i in lst:
                if type(lst) == ListType:
                    sum += self.recur(i)
        else:
            sum += lst
        return sum
            
    def add(self, x, *args):
        if type(x) == type(0):
            self.result += x
        else:
            self.result += self.recur(x)
        if args:
            for j in range(len(args)):
                self.add(args[j])
        return self 

    def subtract(self, x, *args):
        if type(x) == type(0):
            self.result -= x
        else:
            self.result -= self.recur(x)
        if args:
            for j in range(len(args)):
                self.subtract(args[j])
        return self 

md = MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
print md




print "-" * 50



# Part III
class MathDojo(object):
    def __init__(self):
        self.result = 0

    def recur(self, lst):
        sum = 0
        if type(lst) == ListType or type(lst) == TupleType:
            for i in lst:
                if type(lst) == ListType or type(lst) == TupleType:
                    sum += self.recur(i)
        else:
            sum += lst
        return sum
            
    def add(self, x, *args):
        if type(x) == type(0):
            self.result += x
        else:
            self.result += self.recur(x)
        if args:
            for j in range(len(args)):
                self.add(args[j])
        return self 

    def subtract(self, x, *args):
        if type(x) == type(0):
            self.result -= x
        else:
            self.result -= self.recur(x)
        if args:
            for j in range(len(args)):
                self.subtract(args[j])
        return self 

md = MathDojo().add([1],3,4).add([3, 5, 7, 8], (2, 4.3, 1.25)).subtract(2, [2,3], [1.1, 2.3]).result
print md