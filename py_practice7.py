# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:02:52 2020

@author: John
"""

## hacker rank cat and mouse

def catAndMouse(x, y, z):
        cat_a=abs(z-x)
        cat_b=abs(z-y)
        if cat_b>cat_a:
             print("Cat A")
        if cat_b<cat_a:
             print("Cat B")
        else:
             print("Mouse C")
    
    
catAndMouse(1, 3, 2)    

###picking numbers

a=[1,1,2,2,4,4,5,5,5,0,8,9,9,9,9,9,9,9]


def pickingNumbers(a):
    maximum=0
    diff=1
    for num in a:
        n1=a.count(num)
        n2=a.count(num-diff)
        maximum=max(maximum,n1+n2)
    return maximum

pickingNumbers(a)


##hurdle race

def hurdleRace(k, height):
    max_hurdle=max(height)
    dose=max_hurdle-k
    if dose>0:
        return dose
    else:
        return 0
    
    
hurdleRace(7,[2,5,4,5,2 ])   

###PDF Viewer



def designerPdfViewer(h, word):
    char_list=[chr(x) for x in range(ord("a"),ord("z")+1)]
    l=[]
    for w in word:
       l.append((char_list.index(w)))
    m=[]
    for num in l:
        m.append(h[num])
    return max(m)*len(word)

designerPdfViewer(num_list, s)
    
    
###utopian tree

    
    
    
def utopianTree(n):
    x=0
    for i in range(n+1):
        if i%2:
            x*=2
        else:
            x+=1
    return x
    

utopianTree(8)


##angry professor


def angryProfessor(k, a):
    l=[i for i in a if i<=0]
    class_length=len(l)
    if class_length>=k:
            return ("NO")
    else:
            return ("YES")
        
angryProfessor(k, a)

    
##Beautiful days at movies


def beautifulDays(i, j, k):
    count=0
    for num in range(i,j+1):
        i=str(num)
        reverse_i=i[::-1]
        
        if abs(int(i)-int(reverse_i))%k==0:
            count+=1
        else:
            count+=0

    return count
            
        
beautifulDays(20,23, 6)
        


####Viraladvertising

def viralAdvertising(n):
    l=[5]
    a=5
    
    for i in range(0,n-1):
        x=a//2*3
        a=x
        l.append(x)
    m=[(num//2) for num in l]
        
    j=0
    cum_list=[]
    for z in range(0,len(m)):
        j+=m[z]
        cum_list.append(j)
    
    return max(cum_list)

##


