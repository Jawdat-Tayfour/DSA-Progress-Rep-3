# My solution ^_^ 
def BG(o:list[str]) -> int:
    scores = []
    for c in range(len(o)) :
        try:
            scores.append(int(o[c]))
        except ValueError:
            if o[c] == "+":
                scores.append(scores[-1]+scores[-2])
            elif o[c] == "D":
                scores.append(scores[-1]*2)
            elif o[c] == "C":
                scores.pop()
    return sum(scores)
print(BG(['5','2','C','D','+']))                     

#Neet's solution ^_^ 

def BG2(ops:list[str]) -> int:
    stack = []
    for op in ops:
        if op == "+":
            stack.append(stack[-1]+stack[-2])
        elif op == "D":
            stack.append(stack[-1]*2)
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)
print(BG2(['5','2','C','D','+']))         

#Both solution use the exact same Time complexity O(n) and spcae Complexity of O(len(stack))