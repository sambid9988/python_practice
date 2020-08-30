# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:41:00 2020

@author: John
"""



###sum of an array

def sum_2(arr):
    result = 0
    for x in arr:
        result+=x
    return result


a=[1,2,4,10,90,20,50,60]

print("the sum of array is:  {0}".format(sum_2(a)))


## max element of an array

def max_ar(a):
    return max(a)

a=[1,2,4,10,90,20,50,60]
print("the max of array is:  {0}".format(max_ar(a)))


### divide array from a step given and add to the first part from the end
import numpy
arr = np.array([1,2,31,42,51, 60, 7,10,45,21,55])

def arr_split_join(arr,step):
    arr1=arr[:step]
    arr2=arr[step-1:]
    arr2=arr2[1:]
    arr3=np.concatenate((arr2,arr1))
    return arr3
    
arr_split_join(arr, 5)


###Find reminder of array multiplication divided by n
arr=[1,2,3,4,5,6]
arr[2]=5

def arr_mul_rem(arr,s):
    result=1
    for num in arr:
        result*=num
        rem=result%s
       
    return rem
    
    
##check if the array is monotonic

def is_monotonic(arr):
    dx=np.diff(arr)
    return np.all(dx<=0) or np.all(dx>=0)
            
is_monotonic([1,2,3,4,5,9,2])



## swap list first and last element



def swap_list(arr):
    x=arr[-1]
    arr[0]=arr[-1] 
    arr[-1]=x
    return arr
     
a=[10,20,30,40,50,60]
swap_list(arr)     


##swap two positions in a list


def swap_list_pos(arr,pos1,pos2):
    p2=pos2-1
    p1=pos1-1
    arr[p1],arr[p2]=arr[p2],arr[p1]
    return arr

a=[10,24,36,45,50,60,21,31,76,28,31]
swap_list_pos(a, 5, 8)

### remove nth element of a list

def remove_last_ind(arr,n):
    ind=n-1
    arr[ind]=""
    arr=list(filter(None,arr))
    return arr

a=["can", "you",  "can", "a", "can", "?"]
remove_last_ind(a, 3)



###length of list

def length_list(a):
    count=0
    for x in a:
        count+=1
    return count


a=["can", "you",  "can", "a", "can", "?","asd","how","are","you"]
length_list(a)


##check if element exist inside a loop
def num_check(a,num):
    for x in a:
       
        if (x==num) or (x in num):
            return True
        
    return False
      
    
        
test_list = [ 1, 6, 3, 5, 3, 4 ,np.NAN] 
num_check(test_list,np.NAN)    

###reversing a list

def reverse_list(arr):
    arr=arr[::-1]
    return arr

def reverse_list1(arr):
    arr.reverse()
    return arr

test_list = [ 1, 6, 3, 5, 3, 4 ,np.NAN] 
reverse_list(test_list)
test_list = [ 1, 6, 3, 5, 3, 4 ,np.NAN] 
reverse_list1(test_list)



#####cloning a list

def clone(arr):
    arr1=arr.copy()
    return arr1

def clone1(arr):
    arr1=list(arr)
    return arr1

test_list = [ 1, 6, 3, 5, 3, 4 ,np.NAN] 
clone1(test_list)

####count occurences of an element in the list
def count_o(arr,n):
    count=0
    for x in arr:
        if x==n:
            count+=1
    return count
        
    return 0

def count_o1(lst, x): 
    return lst.count(x) 

test_list = [ 1, 6, 3, 5, 3, 4 ,np.NAN,4,5,4,4,55] 
count_o(test_list,4)
count_o1(test_list,4)


##sum of elements in a list

def sum_all(arr):
    return sum(arr)

def sum_all1(arr):
    sum_all=0
    for x in range(0,len(arr)):
        sum_all=sum_all+arr[x]
    return sum_all

test_list = [ 1, 6, 3, 5, 3, 4 ,4,5,4,4,55] 
sum_all(test_list)


###multiply numbers in a list
def multiply_nums(arr):
    result=1
    for num in range(0,len(arr)):
        result*=arr[num]
    return result

test_list = [ 1, 6, 3, 5, 3] 
multiply_nums(test_list)

##finding smallest number in the list

def smallest_num(arr):
        arr.sort()
        result=0
        result=arr[0]
        return result

min(test_list)
test_list = [ 10,201, 6, 3, 5, 3,2] 
smallest_num(test_list)     



######## largest number in the list
def largest_num(arr):
    arr.sort()
    result=0
    result=arr[-1]
    return result

max(test_list)
test_list = [ 10,201, 6, 3, 5, 3,2] 
largest_num(test_list)     


### second largest element

def second_largest(arr):
    arr.sort
    result=0
    result=arr[-2]
    return result

def second_largest1(arr):
    
    arr.remove(max(arr))
   
    arr.sort()
    result=0
    result=arr[-1]
    return result

test_list = [ 10,201, 6, 3, 5, 3,2,300,505,7] 
second_largest1(test_list)


####n largest elements in a list

def n_largest(arr,n):
    arr.sort
    arr1=arr[-n::1]
    return arr1



test_list = [ 10,201, 6, 3, 5, 3,2,300,505,7] 
n_largest(test_list,5)


### print even numbers

def even_nos(arr):
    result=[]
    for num in range(0,len(arr)):
        if arr[num]%2==0:
            result.append(arr[num])
    return result
    
def even_nos1(arr):
    even_nos=list(filter(lambda x:(x%2)==0,arr))
    return even_nos    

test_list = [ 10,201, 6, 3, 5, 3,2,300,505,7] 
even_nos(test_list)
even_nos1(test_list)

###odd numbers 
def odd_nums(arr):
    odd_num=list(filter(lambda x:(x%2)!=0,arr))
    return odd_num
def odd_nums1(arr):
    result=[]
    for num in range(0,len(arr)):
        if arr[num]%2!=0:
            result.append(arr[num])
    return result

test_list = [ 10,201, 6, 3, 5, 3,2,300,505,7] 
odd_nums(test_list)
odd_nums1(test_list)

## print even nos in a range

def even_nos_range(m,n):
    x_range=list(range(m,n))
    result=[]
    for num in range(0,len(x_range)):
        if x_range[num]%2==0:
            result.append(x_range[num])
    return result

even_nos_range(20, 30)

### print even nos and odd nos

def count_even_odd(arr):
    evens=len(list(filter(lambda x:(x%2)==0,arr)))
    odds=len(list(filter(lambda x:(x%2)!=0,arr)))
    print("no of evens:{0}".format(evens))
    print("no of odds:{0}".format(odds))


def count_even_odds(arr):
    even=0
    odd=0
    for num in range(0,len(arr)):
        if arr[num]%2==0:
            even+=1
        else:
            odd+=1
    print("no of evens:{0}".format(even))
    print("no of odds:{0}".format(odd))
    
    
    

test_list = [ 10,201, 6, 3, 5, 3,2,300,505,7,4,3] 
count_even_odds(test_list)
count_even_odd(test_list)




        
        


