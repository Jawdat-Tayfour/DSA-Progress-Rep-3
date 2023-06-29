# My solution 
def Move_zeros(nums:list[int]):
    if not nums : 
        return None     
    l,r = 0 , 0 
    while r<len(nums) and l<len(nums):
        if nums[l] == 0 and nums[r] == 0:
            r+=1
        else:
            temp = nums[r]
            nums[r] = nums[l]
            nums[l]=temp
            l+=1
    return nums         
# O(n) Time Complexity ^_^, O(1) Space Complexity ^_^ , without even watching the explaination. 

#Neet Code Solution 

def Move_zeros2(nums:list[int]):
    l = 0
    for r in range(len(nums)):
        if nums[r]:
            nums[l] , nums[r] = nums[r] , nums[l]
            l+=1
    return nums              

print(Move_zeros([0,1,0,3,12,0,0,1,2,3]))
print(Move_zeros2([0,1,0,3,12,0,0,1,2,3]))

