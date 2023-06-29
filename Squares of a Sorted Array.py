from bigO import BigO

# My solution ^_^ 
def SOASA(n:list[int]):
    i = 0
    while n[0]!=0 :
        if i+1 == len(n):
            i=0
        if abs(n[i]) == abs(n[i+1]):
            if  i+2<len(n):
                if abs(n[i])>abs(n[i+2]):
                    temp = n[i]
                    n[i] = n[i+1]
                    n[i+1] = temp
        elif abs(n[i])>abs(n[i+1]):
            temp = n[i]
            n[i] = n[i+1]
            n[i+1] = temp 
        i+=1    
    for j in range(len(n)):
        n[j] = n[j] * n[j]
    return n               
# I don't feel right about my solution, TIme complexity O(n), Space complexity O(1)         

# Neet Code Solution:

def SOASA2(n:list[int]):
    res = []
    l,r=0, len(n)-1
    while l<=r:
        if n[l]*n[l] > n[r]*n[r]:
            res.append(n[l])
            l+=1
        else:
            res.append(n[r])
            r-=1
    return res[::-1]
        
# O(n) Time , Space O(1) . 



n = [-9,-7,-6,-5,-5,-4,-1,0,3,25,10,11,11,12,18,25,100]
m = [0,1,2,3,4,5,5,6,8]
o = [-8,-7,-8,-6,-5,-5,-4,0]
#My results 
print(SOASA(n))
print(SOASA(m))
print(SOASA(o))
#Neet Code results
print(SOASA2(n))
print(SOASA2(m))
print(SOASA2(o))
"""
My Output:

[0, 1, 9, 16, 25, 25, 36, 49, 81, 100, 121, 121, 144, 324, 625, 625, 10000]
[0, 1, 4, 9, 16, 25, 25, 36, 64]
[0, 16, 25, 25, 36, 49, 64, 64]

Neet Code's Output:

[0, 1, 9, 16, 25, 25, 36, 49, 81, 100, 121, 121, 144, 324, 625, 625, 10000]
[0, 1, 4, 9, 16, 25, 25, 36, 64]
[0, 16, 25, 25, 36, 49, 64, 64]
"""