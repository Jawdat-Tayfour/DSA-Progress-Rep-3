# My solution ^_^ 
def VPS(n:int):
    first , last =1,n 
    while first<=last:
        mid= (first + last)//2
        if mid * mid == n :
            return True 
        else:
            last = mid -1
    return False 
# Binary search because the square root of a number is always below number//2 , Time compelxity of binary search is O(log(n))

# Neet code solution 

def VPS2(n:int):
    for i in range(1,n+1):
        if i*i == n :
            return True 
        if i*i > n :
            return False 

# This one is in O(sqrt(n)) Time complexity 

def VPS3(n:int):
    l,r = 1,n 
    while l<=r:
        mid = (l+r)//2 
        if mid * mid > n:
            r = mid-1
        elif mid*mid <n:    
            l = mid + 1
        else:
            return True 
    return False 

#Time compelxity of binary search is O(log(n))

print(VPS(14),
VPS(16),
VPS2(14),
VPS2(16),
VPS3(14),
VPS3(16))        