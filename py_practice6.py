# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:02:42 2020

@author: John
"""

##birthday chocolate
def getWays(squares, d, m):
    cnt = 0
    q = squares[:m-1]
    for ele in squares[m-1:]:
        q.append(ele)
        if (sum(q) == d):
            cnt += 1
        q.pop(0)
    return cnt

getWays([1 ,2 ,1 ,3 ,2], 3, 2)


##divisible sum of pairs
import itertools as it

def divisibleSumPairs(n, k, ar):
    results=[sum(i) for i in list(it.combinations(ar, 2))]
    return len([i for i in results if i%k==0])


n=6 
k=3
ar=[1 ,3 ,2 ,6 ,1 ,2]
divisibleSumPairs(n, k, ar)


##migratory birds
import collections


def migratoryBirds(arr):
    counter=collections.Counter(arr)
    max_freq=[i for i in counter if counter[i]==max(counter.values())]
    return min(max_freq)

migratoryBirds([1,1,1,2,2,2])

##Day of the programmer

def dayOfProgrammer(year):
    if(year==1918):
        return "26.09.1918"
    if (year%4==0) and (year<1918 or year%400==0 or year%100!=0):
        return print("12.09.%d"%year)
    else:
        return print("13.09.%d"%year)


dayOfProgrammer(1924)  

##BonAppetit

def bonAppetit(bill, k, b):
    bill.pop(k)
    bill_sum=sum(bill)
    overcharged=(bill_sum/2)-b
    if overcharged==0:
        return "Bon Appetit"
    if overcharged<0:
        return abs(int(overcharged))
    
bonAppetit([3,10,2,9], 1, 8)    
    
    
##sockMerchant
        
def sockMerchant(n,ar):
    my_set=set(ar)
    count=0
    for i in my_set:
        if ar.count(i)//2>=1:
            count+=ar.count(i)//2
    return count




###page count



def pageCount(n, p):
    from_front=p//2
    from_back=n//2-p//2
    return min(from_front,from_back)
    
    
    

pageCount(6,5)


##valley count

def countingValleys(steps, path):
    level=valleys=0
    for direction in path:
        if direction=="U":
            level+=1
            if level==0:
                valleys+=1
        else:
            level-=1
    return valleys

countingValleys(8, "UDDDUDUU")


###electronics shop

















            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    







