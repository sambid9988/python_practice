# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 19:14:46 2020

@author: John
"""


## grading students 


def gradingStudents(grades):
    l=[]
    for num in grades:
        if num>=38:
            if num%5==3:
                num+=2
            if num%5==4:
                num+=1
            l.append(num)
        if num<38:
            l.append(num)
    return l
            
   



gradingStudents([74,66,39,33])         
    

##count apples and oranges

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples=[x+a for x in apples]
    oranges=[x+b for x in oranges]
    count_a=0
    count_o=0
    l=[]
    for num in apples:
        if num>=s and num<=t:
            count_a+=1
            l.append(count_a)
    for num in oranges:
        if num>=s and num<=t:
            count_o+=1
            l.append(count_o)
            
    return print(*l)
    
            
countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])
        
    
#####    kangaroo


## x1+y*v1 = x2+y*v2 (y is the number of jumps)
## x1-x2 / v2-v1

def kangaroo(x1, v1, x2, v2):
    if v1>v2 and (x1-x2)%(v2-v1)==0:
        return ("YES")
    else:
        return ("NO")

kangaroo(1571 ,4240, 9023, 4234)


## between two sets
import numpy as np
import math
from functools import reduce



def getTotalX(a, b):
    x=np.gcd.reduce(a)
    y=np.lcm.reduce(b)
    count=0
    for num in range(y,x+1,y):
        if np.gcd(num,x)==num:
            count+=1
    return count

getTotalX(a, b)


## print fizzbuzz for 15
def fizzbuzz(n):
    for num in range(1,n+1):
        if num%5==0 and num%3==0:
            print ("fizzbuzz")
            continue
        if num%3==0:
            print("fizz")
            continue
        if num%5==0:
            print("buzz")
            continue

        else:
            print(num)
        
        
  
fizzbuzz(15)     
###
a=[1,2,3,4,6]
min(a)
max(a)
a=[10, 5 ,20, 20, 4, 5, 2, 25, 1]



def breakingRecords(score):
    count_max=count_min=0
    min_score=max_score=score[0]
    for num in score[1:]:
        if num>max_score:
            count_max+=1
            max_score=num
        if num<min_score:
            count_min+=1
            min_score=num
    l=[]
    l.append(count_max)
    l.append(count_min)
    return print(*l)

            
            
  
a=[3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
breakingRecords(a)
    
    
    
    
    
    
        
