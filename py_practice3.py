# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 20:08:25 2020

@author: John
"""


##postive nos

def positive_nos(arr):
    result=[]
    for num in range(0,len(arr)):
        if arr[num]>0:
            result.append(arr[num])
    return result
            
def positive_nos1(arr):
    result=[x for x in arr if x>0]
    return result
    
def positive_nos2(arr):
    result=list(filter(lambda x:x>0 , arr))
    return result
    

arr=[1,2,3,4,-1,-2,-4,-7]
positive_nos(arr)
positive_nos1(arr)
positive_nos2(arr)

##negative numbers
def negative_nos(arr):
    result=[x for x in arr if x<0]
    return result
    
def negative_nos1(arr):
    result=list(filter(lambda x:x<0 , arr))
    return result

negative_nos(arr)
negative_nos1(arr)

import numpy
### positive numbers within a range

def pos_num_range(m,n):
    arr=np.concatenate((m,n))
    #arr=m+n
    result=[x for x in arr if x>0]
    return result

arr=[1,2,3,4,-1,-2,-4,-7]
arr1=[11,12,13,14,-11,-12,-14,-17]
pos_num_range(arr,arr1)


### negative numbers within a range

def neg_num_range(m,n):
    arr=m+n
    result=list(filter(lambda x:x<0 , arr))
    return result

arr=[1,2,3,4,-1,-2,-4,-7]
arr1=[11,12,13,14,-11,-12,-14,-17]
neg_num_range(arr,arr1)



###remove numbers

def remove_even(arr):
    for num in arr:
        if num %2==0:
            arr.remove(num)
    return arr

arr=[1,2,3,4,-1,-2,-4,-7]
remove_even(arr)
    

def remove_nums(arr,rem):
    result=[x for x in arr if x not in rem]
    return result
   
arr1=[11,12,13,14,-11,-12,-14,-17] 
rem=[11,13]

remove_nums(arr1,rem)


##remove empty tuples
def remove_tups(arr): 
    tuples =list(filter(None, arr))
    return tuples 

arr = [(), ('ram','15','8'), (), ('laxman', 'sita'),  
          ('krishna', 'akbar', '45'), ('',''),()] 

print (remove_tups(arr)) 


## print duplicates

def dups(arr):
    result=list(set(list(filter(lambda x:arr.count(x)>1, arr))))
    return result


arr1=[11,12,13,14,-11,-12,-14,-17,11,12,13,14] 
dups(arr1)



###cumulative sum of a list

arr = [10, 20, 30, 40, 50]

def cum_sum(arr):
    result=[]
    numx=0
    for num in range(0,len(arr)):
        numx+=arr[num]
        result.append(numx)
    return result
    

cum_sum(arr)




### sort values of second list based on second list
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"] 
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1] 

x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"] 
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1] 
  


           
def sort_list(arr1,arr2):
    zipped_pairs=zip(arr1,arr2)
    
    z=[x for _,x in sorted(zipped_pairs)]
    return z

sort_list( y,x )

###check if palindrome or not

def palindrome(s):
    x=s[::-1]
    print(x)
    if x==s:
        return True
    else:
        return False
    
palindrome("radax")

###reverse words of a give string

def reverse_string(s):
    string=s.split()
    string=string[::-1]
    string=" ".join(string)
    return string

string="a s d aass fff gsfa"
reverse_string(string)

##replace ith character of the string 

def replace_char(s,num):
    s= s.replace(s[num],"",1)
    return s
string="abcdefghihhhhh"
replace_char(string, 7)


###check if a substring present in string
import re
def check_sub_str(sub_str,string):
    if re.search( sub_str,string):
        print("yes substring is present in the string")
    else:
        print("not present")
        
check_sub_str("hello", "hello string hi") 


def check_sub_str1(string,sub_str):
    if (string.find(sub_str)==-1):
        print("no")
    else:
        print("yes")

string = "geeks for geeks"
sub_str ="geek"
check_sub_str1(string, sub_str) 

##length of a string

def length_str(string):
    return len(string)

def length_str1(string):
    count=0
    for s in string:
        
        count+=1
    
    return count

length_str1("asd   asd")


###print words with even length

def even_length_words(string):
    string=string.split()
    for s in range(0,len(string)):
        if (len(string[s])%2==0):
            new_string=string[s]
            print(new_string)
    
    

even_length_words("This is a python language")


###check if vowels present
x="This is a python language"
x.lower()
def vowel_check(string):
    string=string.lower()
    vowels=["a","e","i","o","u"]
    for char in string:
        if char in vowels:
            return True
        else:
            return False
 
x="ABeeIghiObhkUul"       
vowel_check(x)       

##count number of vowels

def count_vowels(string):
    string=string.lower()
    string=string.replace(" ","")
    vowel_set=set("aeiouAEIOU")
    count=0
    for char in string:
        if char in vowel_set:
            count+=1
            
    return count

count_vowels("sed uziasd")


## remove duplicates from a string

def remove_dup(string):
    string=string.lower()
    string=set(string)
    string=" ".join(string)
    return string
    
        
remove_dup("string str i")        
        

## check if any special character are there or not

def check_special_char(string):
    pattern=re.compile("[@_!#$%^&*()<>?/\|}{~:]")
    if (pattern.search(string)==None):
        return False
    else:
        return True

check_special_char("sdasda")    


###find words which are greater than length k

def words_big_length_k(string,k):
    string=string.split()
    l=[]
    for char in range(0,len(string)):
        if len(string[char])>k:
            l.append(string[char])
    
    return l
        
            
words_big_length_k( "string is fun in python", 3)
        

##find uncommon words
def uncommon_words(string1,string2):
    string1=string1.lower().split()
    string2=string2.lower().split()
    l=[]
    m=[]
    for char in string1:
        
        if char not in string2:
            l.append(char)
                
    for chars in string2:
        if chars not in string1:
            m.append(chars)
    n=l+m
    return n
                
                
    
    

A = "Geeks for Geeks" 
B = "Learning from Geeks for Geeks"    

A = "apple banana mango" 
B = "banana fruits mango"
    
uncommon_words(A, B)


##swap , and . in a string

def swap_case(string):
    string1=string.replace(",","x")
    string2=string1.replace(".",",")
    string3=string2.replace("x",".")
    return string3

swap_case("102.456,204")

