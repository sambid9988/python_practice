# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:50:33 2020

@author: John
"""


# save the prisoner

#n is of prisoners, m is sweets,s is position
def saveThePrisoner(n, m, s):
    m %= n
    s += m - 1
    s %= n 
    if s == 0:
        return n
    else:
        return s

##circular array rotation

#a=array, k=rotation count and q=query num


from collections import deque

def circularArrayRotation(a, k, queries):
    c=deque(a)
    c.rotate(k)
    l=[]
    for num in queries:
        l.append(c[num])
    return l
        
circularArrayRotation([1,2,3], 2, [0,1])        
    
    
## sequence equation


def permutationEquation(p):
    a=list(range(1,len(p)+1))
    ind_a=[]
    for num in range(0,len(a)):
        ind_a.append(p.index(a[num]))
    
    
    ind_a=[x+1 for x in ind_a]
    ind_b=[]

    for num in range(0,len(ind_a)):
        ind_b.append(p.index(ind_a[num]))

    ind_b=[x+1 for x in ind_b]
    return ind_b

permutationEquation([4,3,5,1,2])


###jumping on the clouds


def jumpingOnClouds(c, k):
    energy = 100 #initial energy
    n=len(c)
    i = k % n #initial jump from 0
    energy -= c[i] * 2 + 1 #initial energy loss

    while i != 0:
        i = (i + k) % n
        energy -= c[i] * 2 + 1
    return energy
    
c=[0,0,1,0,0,1,1,0]
jumpingOnClouds(c, 2)

##find digits
def findDigits(n):
    str_n=str(n)
    count=0
    for num in str_n:
        if int(num)!=0 and int(str_n)%int(num)==0:
            count+=1
        
    return count

findDigits(1024)
