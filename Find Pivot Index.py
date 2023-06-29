# My solution ^_^

def FPI(nums:list[int]):
    m = 0
    sumsum = sum(nums)
    leftSum =0   
    while m<len(nums):
        rightSum = sumsum - leftSum - nums[m]
        if leftSum == rightSum :
            return m 
        leftSum+=nums[m]
        m+=1
    return -1     
# Time complexity O(n) Space Complexity O(1) , I watched the explaination for this one, because when I tried to do it on my own 
# I ended up with O(n**2) Time complexity which is just sad. Anyways let's how Neet is gonna implement his expalinations.

#Neet Code Solution 

def FPI2(nums:list[int]):
    total = sum(nums)
    leftSum = 0 
    for i in range(len(nums)):
        rightSum = total - nums[i] - leftSum
        if leftSum == rightSum:
            return i 
        leftSum+=nums[i]
    return -1     

# yeah kinda the same as I wrote, I hate to feel like I'm just a mockingbird, but it is what it is, see ya 2morrow X_X.
print(FPI2([1,7,3,6,5,6]))
print(FPI([1,7,3,6,5,6]))
