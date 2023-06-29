    # My solution %_% 
class TreeNode():
    def __init__(self,value = None,left = None ,right = None ):
        self.value = value
        self.right = right 
        self.left = left 
def CSFBT(root:TreeNode):
    if not root:
        return ()
    return root.value,CSFBT(root.left),CSFBT(root.right)
#(1, (2, (4, (), ()), ()), (3, (), ())) could not do it properly 

# Neet's solution 

def CSFBT2(root:TreeNode):
    res = []
    def preorder(root):
        if not root:
            return
        res.append("(")
        res.append( str(root.value))
        if not root.left and root.right:
            res.append("()")
        preorder(root.left)
        preorder(root.right)
        res.append(")")
    preorder(root)
    return "".join(res)[1:-1]
# 1(2(4))(3) that's the output that I should've gotten but, these things happen, I learned my lesson. and that my friends is the last video in the EASY playlist. 
# let's move on to the next level.
#P.S. both codes run in O(n) Time complexity.
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print(CSFBT2(root))
print(CSFBT(root))