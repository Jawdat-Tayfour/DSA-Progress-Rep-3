# I know how to solve this one in linear time, but I will just learn the binary search one. 
def AC(n:int):
    l,r = 0 , n 
    res = 0
    while l<=r:
        mid = (l+r)//2
        coins_needed = (mid/2)*(mid+1)
        if coins_needed <= n :
           res = max(res,mid)
           l = mid +1 
        else:
            r = mid -1 
    return res                 
print(AC(21))        
# That is my implementation of Neet Code explaination. This Solution follows Gauss fourmela it gives us O(1) Space and O(n) Time complexity 
#Neet Code Solution 
 
def AC(n:int):
    l,r = 1,n 
    res = 0
    while l<=r:
        mid = (l+r)//2
        coins = (mid/2)*(mid+1)
        if coins > n : 
            r = mid -1 
        else : 
            l = mid +1 
            res = max(res,mid)     
    return res 
# We implemented the exact same way, I'm actually so proud of myself, this man is a legend in problem solving. 