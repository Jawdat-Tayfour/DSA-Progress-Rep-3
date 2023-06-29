# My solution x_x 
class TreeNode():
    def __init__(self,value=None,right=None,left=None):
        self.value = value
        self.right = right
        self.left  = left 
        self.visited = False 
def IRBTIT(root:TreeNode,res = [] ):
    node = TreeNode()
    if not root:
        return None
    current = root 
    
    IRBTIT(current.left,res)    
    res.append(current.value)
    IRBTIT(current.right,res)

    return res 
# This the recuresive solution that has a time complexity of the number of node in the tree. O(n) Time, O(n) Space due to the recursive calls. 
def IRBTIT2(root:TreeNode):
    current = root 
    stack = []
    res =[]
    while True :
        if current is not None:
            stack.append(current)
            current = current.left
        elif (stack):
            current = stack.pop()
            res.append(current.value)
            current = current.right
        else:
            break 
    return res         
# I learned this soution from geeks for geeks and adjusted it a bit to fit the way I want to see the output. O(n) Time, O(n) Space. 

#Neet Code Recursive Solution 

def IRBTIT3(root:TreeNode):
    res = []
    def indorder(root):
        if not root:
            return
        indorder(root.left)
        res.append(root.value)
        indorder(root.right)
    indorder(root)
    return res     

#Neet Code Iterative Solution 

def IRBTIT4(root:TreeNode):
    res = []
    stack = []
    cur = root 
    while cur or stack : 
        while cur :
            stack.append(cur)
            cur = cur.left 
        cur = stack.pop()
        res.append(cur.value)
        cur = cur.right
    return res         
# So here you go 4 solution for the same problem. with ALMOST the same time and space compelxity. 
# Neet code solution are verified

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
print(IRBTIT2(root))
print(IRBTIT(root))
print(IRBTIT3(root))
print(IRBTIT4(root))