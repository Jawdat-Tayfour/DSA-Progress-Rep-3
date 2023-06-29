# My solution *_* 

def NGEI(nums1:list[int],nums2:list[int]):
    l,r = 0,0 
    res =[]    
    while l<len(nums1):
        if nums1[l] != nums2[r]:
            r+=1
        else:
            while r<len(nums2):
                if r == len(nums2)-1 and nums2[r]<=nums1[l]:
                    res.append(-1)
                    r = 0
                    break
                elif nums2[r] <= nums1[l]:
                    r+=1
                elif nums2[r] > nums1[l]:
                    res.append(nums2[r])
                    r = 0
                    break
            l = l+1   
    return res 
# This one will take up to O(n*m) Time Complexity which may make it a bad solution. I will see Neet's solution.

# Neet's first solution 

def NGEI2(nums1:list[int],nums2:list[int]):
    nums1Idx = {n:i for i,n in enumerate(nums1)}
    res = [-1] * len(nums1)
    for i in range(len(nums2)):
        if nums2[i] not in nums1Idx:
            continue
        for j in range(i+1,len(nums2)):
            if nums2[j]>nums2[i]:
                idx = nums1Idx[nums2[i]]
                res[idx] = nums2[j]
                break 
    return res         
#O(n*m) Time Complexity and O(n) Space Complexity 


# Now for the O(n+m) Soultion 

def NGEI3(nums1:list[int],nums2:list[int]):
    nums1Idx = {n:i for i,n in enumerate(nums1)}
    res = [-1] * len(nums1)
    stack = []
    for i in range(len(nums2)):
        cur = nums2[i]
        while  stack and cur > stack[-1]:
            val =stack.pop()
            idx =nums1Idx[val]
            res[idx] = cur 
        if cur in nums1Idx:
            stack.append(cur)
    return res             
 

print(NGEI([4,2] , [1,1,1,2,4]))    
print(NGEI2([4,2] , [1,1,1,2,4]))    
print(NGEI3([4,2] , [1,1,1,2,4]))    





# [4,1,2] , [1,3,4,2]
#  l             r   
#  l               r
#  l               r>l == False and r == len(nums2) -1 , we add -1 to the res  
#    l       r 
# nums1[l] == nums2[r] , we move r and  find an element that is next to one and greater than 1 and add it to res 
#    l         r    in our case 3 statsfies the  condetions we add to res and reset r 
#      l      r
# now l is 2 and r is 1 we move r until we find l 
#      l           r
# we find it but there is nothing after it so we add -1 to the result and exit the loop and retunr our res 
# [-1,3,-1]