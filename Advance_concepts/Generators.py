
''' Generators are the functions,which has yield keyword in it, which returns an iterator address '''

def even_num_gen():
    num=0
    while True:
        yield num
        num+=2
var=even_num_gen()
print(next(var))
print(next(var))
print(next(var))
print(next(var))

print()

############################################################################

def odd_num_gen():
    num=1
    while True:
        yield num
        num+=2
var=odd_num_gen()
print(next(var))
print(next(var))
print(next(var))
print(next(var))

print()

###########################################################################

def prime_gen():
    num=2
    while True:
        for number in range(2,num):
            if num%number==0:   
                break
        else:
            yield num
            
        num+=1
var=prime_gen()
print(next(var))
print(next(var))
print(next(var))
print(next(var))

print()

###########################################################################

def multiples_gen(num):
    factor=1
    while True:
        yield num*factor
        factor+=1
var=multiples_gen(8)
print(next(var))
print(next(var))
print(next(var))
print(next(var))

print()

###########################################################################

def fib_seq_gen():
    num1,num2=0,1
    while True:
        yield num1
        num1,num2=num2,num1+num2
var=fib_seq_gen()
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))

print()

#########################################################################

def perfect_gen():
    num=1
    while True:
        for number in range(1,int(num**0.5)+1):
            if num/number==number:
                yield num
        num+=1
var=perfect_gen()
print(next(var))
print(next(var))
print(next(var))
print(next(var))

print()

#############################################################################

def armstrong_gen():
    num=1
    while True:
        length=len(str(num))
        arms=0
        number=num
        while number!=0:
            last_digit=number%10
            arms+=last_digit**length
            number//=10
        else:
            if arms==num:
                yield arms
                # num+=1
        num+=1
        arms=0
        length=len(str(num))
        number=num
var=armstrong_gen()
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))




