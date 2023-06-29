# My solution ### I'm not solving on leetcode so I'll do the guess function myself. 
def guess(n:int,p:int):
    if n>p:
        return 1
    elif n<p:
        return -1 
    else:
        return 0 
# Now to the algorithm which is basically a binary search. 

def GNHOL(n:int,q:int):
    l = n 
    f = 1
    while f<l:
        mid = (l+f)//2
        if guess(mid,q) == 0:
            return mid
        if guess(mid,q) == -1:
            f = mid+1
        if guess(mid,q) == 1:
            l = mid-1
    return "Number does not exist in the range"     
print(GNHOL(50,4))
# Yessir , O(log(n)) Time complexity, O(1) Space Complexity ^_^. tbh it was easy. 

# Neet Code Solution 

def GNHOL2(n:int,q:int):
    l,r =1,n
    while l<r:
        m = (l+r)//2
        res = guess(m,q)
        if res > 0:
            r= m-1
        elif res < 0:
            l = m+1 
        else:
            return m
        
print(GNHOL2(50,4))
# The Exact same solution , 10 more easy problems and we're good to level up fellas, wish me luck. I'm also learning Django.

    