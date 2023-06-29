# My solution 
def ME(n:list[int]):
    if not n : 
        return None
    l = len(n)
    first = 0 
    second = 0 
    counter = 0
    while first < l :
        if second >= l :
            second = 0
            first +=1
        if n[first] == n[second]:
            counter += 1 
            if counter > (l//2):
                return n[first]
        second+=1    
    return None 
print(ME([1,2,3,3,2,2,1,1,1,1,2,2,2,2]))
# As required, O(n) Time complexidty, O(1) Space Complexity, And now I wanna watch Neet code explaination. ^_^

# Neet Code is going to solve it in two ways, the first one with O(N)for both time and space and the other one with O(1) spcae and O(n) Time 
#let's start with the first one. 

def ME2(nums:list[int]):
    count = {}
    res,maxCount = 0,0
    for n in nums :
        count[n]= 1 + count.get(n,0)
        res = n if count[n]>maxCount else res 
        maxCount = max(count[n],maxCount)
    return res     
print(ME2([1,2,3,3,2,2,1,1,1,1,2,2,2,2,2]))

#Boyer-moore Algorithm. 

# Neet Code Solution 2 

def ME3(nums:list[int]):
    res,count = 0,0
    for n in nums:
        if count == 0 :
            res = n 
        count+=(1 if res==n else -1)
    return res 

print(ME3([1,2,3,3,2,2,1,1,1,1,2,2,2,2,2]))
