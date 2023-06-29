import math 
from collections import Counter
# My solution ^_^ 
def MNOB(n:str): 
    Balloons =['b','a','l','o','n'] # balloon = 7 
    counter = 0
    for c in n :
        if c in Balloons:
            counter+=1     
    return counter // 7                 
# O(n) Time and O(1) Space Complexity 
print(MNOB('balloonsodsadasbdaallsoonsobnall'))  

# Neet Code Solution 
def MNOB2(t:str):
    countText=Counter(t)
    balloon = Counter("balloon")
    res = len(t)
    for c in balloon : 
        res = min(res,countText[c]// balloon[c])
    return res     
print(MNOB2('balloonsodsadasbdaallsoonsobnall')) 
# O(n) Time , O(1) Space , but I feel like my solution is kinda simpler than his. idk. lemme know comment down.  
