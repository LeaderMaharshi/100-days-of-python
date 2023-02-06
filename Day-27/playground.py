def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(sum)

add(2,3,4,5,6,7,8,10)

def cal(a,b):
    print(a-b)
    
cal(2,1)

def calculate(n, **kwargs):
    # print(kwargs)
    # print(kwargs['add'])
    n += kwargs['add']
    n *= kwargs['multiply'] 
    print(n)   

calculate(2, add=3, multiply=5) 

class Cars:
    
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
    
my_car = Cars(make="Nisson")

print(my_car.make)