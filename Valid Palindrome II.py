# My solution 
def VPII(s:str)->bool:
    l,r = 0,len(s)-1
    _mismatch_count = 0
    while l<=r:
        if s[l] != s[r]:
            _mismatch_count+=1
            break        
        l+=1
        r-=1
    if _mismatch_count == 1:
        p,q = [0]*len(s),[0]*len(s)
        q =list(s) 
        p = list(s) 
        q.pop(r)
        p.pop(l)
        return p == p[::-1] or q == q[::-1]
    else:
        return True 
print(VPII("levels")) 
# solution with time complexity O(n), the algorithm is simple,
# scan until you find a mismatch create two copies of the string without the char that caused the mismatch then check if one of the copies a palindrome. 
# and if you didn't find a mismatch that means we have a palindrome. 
  
# Now to Neet's Solution 

def VPII2(s:str)-> bool:
    l,r = 0 , len(s)-1
    while l<r:
        if s[l] != s[r] :
            skipL,skipR = s[l+1:r+1],s[l:r]
            return skipL == skipL[::-1] or skipR == skipR[::-1]
        l+=1
        r-=1    
    return True 
print(VPII2("levels"))    

# Kind of the same algorithm but he puts it much simpler form. and a bit faster I think.