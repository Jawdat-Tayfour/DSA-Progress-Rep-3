# My solution &_& 
def RS(s:list[str]) -> list[str]:
    return s[::-1]
print(RS(['c','a','k','e']))
# My solution  2 #_#
def RS2(s:list[str]) -> list[str]:
    l,r = 0, len(s) -1 
    while l<=r:
        temp = s[l] 
        s[l] = s[r]
        s[r] = temp 
        r-=1
        l+=1
    return s      
print(RS2(['c','a','k','e']))
# My solution  3 ^_^
def RS3(s:list[str]) -> list[str]:
    j = len(s) -1 
    for i in range (0,len(s)//2):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        j-=1
    return s         
print(RS3(['c','a','k','e']))
# I can go forever and ever with this. lol.

# Neet Code solution 2
def RS4(s:list[str]) -> list[str]:
    stack = []
    for c in s :
        stack.append(c)
    i=0
    while stack:
        s[i] = stack.pop()
        i+=1
    return s     
print(RS4(['c','a','k','e']))
# Neet code solution 1  is just like the two pointer method above 

# Neet code solution 3 
def RS5(s:list[str]) -> list[str]: 
    def revrse(l,r):
        if l<r:
            s[l],s[r] = s[r],s[l]          
            revrse(l+1,r-1)
    revrse(0,len(s)-1)
    return s 
print(RS5(['c','a','k','e']))

