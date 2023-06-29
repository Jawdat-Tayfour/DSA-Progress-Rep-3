# My solution ^_^
def SN(numbers:list[int]):
    l = 0 
    r = 0 
    counter = 0
    while l<len(numbers):
        if numbers[l] == numbers[r]:
            r+=1
            counter+=1
        else:
            r+=1
        if counter == 2 :
            counter = 0 
            l+=1
            r = 0
        if r == len(numbers) and counter == 1 :
            break
    return numbers[l]            
# O(n) Time complexity and O(1) Space ^_^ Now to Neet Code explaination and solution. 

print(SN([2,2,1,6,1,4,4,5,6,5,3]))

# Neet Code Solution (Bit Manipulation method using XOR)

def SN(numbers:list[int]):
    res = 0 # Because n XOR 0 Always equals : n 
    for n in numbers:
        res = n ^ res
    return res
# Linear Time as well as constant space. Brilliant! it's always fun to know things that are out of your box.