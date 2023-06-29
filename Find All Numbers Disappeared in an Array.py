# My solution ^_^
def FANDIAA(nums:list[int]):
    n = len(nums)
    nonA = []
    for i in range (1,n):
        if i not in nums: 
            nonA.append(i)
    return nonA
print(FANDIAA([4,3,2,7,8,2,3,1]))      
 # Ok so that is my first shot at the problem, I think we can do better than O(n**2)      

# Neet Code Solution . 

def FANDIAA3(nums:list[int]):
    for n in nums:
        i = abs(n)-1
        nums[i] = -1 * abs(nums[i])
    res=[]
    for i,n in enumerate(nums):
        if n > 0:
            res.append(i+1)
    return res             
print(FANDIAA3([4,3,2,7,8,2,3,1]))      
#O(1) Space & O(n) Time complexity 
