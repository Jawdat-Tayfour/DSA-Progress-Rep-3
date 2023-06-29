# My solution ^_^ 
def BS(nums:list[int],t:int) -> int:
    first =  0 
    last = len(nums) -1 
    while first<=last:
        mid = (first+last)//2
        if nums[mid]>t:
            last = mid -1 
        elif nums[mid]<t:
            first = mid +1 
        else:
            return mid 
    return -1            
print(BS([-1,0,3,5,9,12],2))
# he said as if you are doing it in your sleep, I did in less than 50 seconds.
 
