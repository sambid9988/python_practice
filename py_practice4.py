# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:53:12 2020

@author: John
"""

###hackerrank

###diagonal difference

def diagonalDifference(arr):
    sum1=0
    sum2=0
    length_ar=len(arr)
    for num in range(0,length_ar):
        sum1+=arr[num][num]
        sum2+=arr[num][length_ar-num-1]
        diff=abs(sum1-sum2)
    return diff




arr=[[1,2],[4,5]]
diagonalDifference(arr)


###plus minus

def plusMinus(n,arr):
    count_pos=0
    count_neg=0
    count_zero=0
    length_arr=len(arr)
    for num in arr:
        if num>0:
            count_pos+=1
        if num<0:
            count_neg+=1
        if num==0:
            count_zero+=1
    prop_pos=round(count_pos/length_arr,6)
    prop_neg=round(count_neg/length_arr,6)
    prop_zero=round(count_zero/length_arr,6)
    return prop_pos,prop_neg,prop_zero

plusMinus(6,[-4,3,-9,0,4,1])


##staircase
 

def staircase(n):
    for num in range(1,n+1):
        print(("#"*num).rjust(n))
        
staircase(5)        
        
            
##min max function
arr=[1,2,3,4,5]           

def min_max(arr):
    arr1=arr.copy()
    arr.remove(max(arr))
    min_sum=sum(arr)
    arr1.remove(min(arr1))
    max_sum=sum(arr1)
    return print(min_sum,max_sum)

min_max(arr)


##birthday cake candles count


def birthdayCakeCandles(candles):
    max_height=max(candles)
    total_count=candles.count(max_height)
    return total_count
    
birthdayCakeCandles(arr)
    

##time conversion




def timeConversion(s):
    x,y,z=s.split(":")
    x=int(x)%12+(z.find("PM")!=-1)*12
    z=z.replace("PM","").replace("AM","")
    y=int(y)
    z=int(z)
    print ('{:02}:{:02}:{:02}'.format(x, y, z))
    #print ("%02d:%02d:%02d" %(x,y,z))
    
   
    
  
s="07:05:45PM"
timeConversion(s)
    




