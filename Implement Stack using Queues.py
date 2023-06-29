# I'm not gonna solve it, this matter is new to me, 
    #I know what a stack is,
        #and I know what a queue is,
            # And I know how to use them.I also know their varaints but, the implementation is just another thing for me.
# thanks for understanding.
# I'll write out Neet Code solution to this.  ^_^
from collections import deque
class mystack():
    def __init__(self):
        self.q = deque()
    def push(self,value:int):
        self.q.append(value)
    def top(self):
        return self.q[-1]
    def empty(self):
        return len(self.q)==0
    def pop(self):
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()            
#it turned to be easy, but I'd ask, when in hell should I do that ?. haha.    