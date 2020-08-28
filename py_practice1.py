# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 18:35:57 2020

@author: John
"""

# -*- coding: utf-8 -*-

    
## sum of two nums
num1=input("First num:  ")
num2=input("second num: ")
sum=float(num1)+float(num2)

print("sum of {0} and {1} is {2}".format(num1,num2,sum))


## factorial
def factorial(n):
    return 1 if (n==0 or n==1) else n*factorial(n-1)

x=factorial(5)


##simple interest
def simple_interest(p,t,r):
    print("the principle is",p)
    print("the time is",t)
    print("the rate is",r)
    si=(p*t*r)/100
    
    return print("The simple interest is {}".format(si))

##compund interest

def compound_interest(p,t,r):
    print("the principle is",p)
    print("the time is",t)
    print("the rate is",r)
    amount=p*pow((1+(r/100)),t)
    ci=amount-p
    return print("the compound interest is{0}".format(ci))
    

#####armstrong number
def isarmstrong(x):
    result=0
    snum=(str(x))
    slen=len(snum)
    for digit in snum:
        result+=int(digit)**slen
        if result>x:
            return False
    if result!=x:
        return False
    return True
        

##finding area of circle

def area_circle(r):
    pi=3.14
    area=pi*r*r
    return print("area of the circle is {0}".format(area))
        
        
        
##check number is prime or not

def prime_num(a):
    for x in range(2,a):
        if a%x==0:
            print("this is a not prime number")
            break
    else:
        print("the number is a prime")
          
    
    
###fibonacci

def fib(n):
    if n<0:
        print("Incorrect Input")
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
  
##check if fibonnaci
def is_fibonacci(n):
    return n >= 0 and (n==0 or sqrt( 5*n*n - 4).is_integer() or sqrt( 5*n*n + 4).is_integer())


##square of numbers
def squares_n(x):
    result=0
    for num in range(1,x+1):
        result+=num*num
    return result
        



