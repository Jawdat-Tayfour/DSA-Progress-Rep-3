# My Solution ^_^
class TreeNode():
    def __init__(self,value=None,left=None,right=None ):
        self.value = value 
        self.right = right  
        self.left = left 


        
def PS(root:TreeNode,PS1:int,new_max = 0):
    if not root : 
        return False 
    new_max += root.value
    if new_max == PS1:
        return True 
    if new_max<PS1:
        return PS(root.left,PS1,new_max) or PS(root.right,PS1,new_max)
    return False 
# Time complexity is O(n), Space Complexity is O(1)

#Neet Code Solution

def hasPathSum(root:TreeNode,TargetSum:int):
    def dfs(node:TreeNode ,current_total):
        if not node :
            return False 
        current_total+=node.value
        if not node.left and not node.right :
            return current_total == TargetSum
        return dfs(node.right,current_total) or dfs(node.left,current_total)
    return dfs(root,0)

# Time complexity is O(n), Space Complexity is O(1)

# Create a binary tree
#        5
#       / \
#      4   8
#     /   / \
#    11  13  4
#   /  \      \
#  7    2      1

# Define the tree nodes
node7 = TreeNode(7)
node2 = TreeNode(2)
node11 = TreeNode(11, node7, node2)
node4_left = TreeNode(4, node11)
node1 = TreeNode(1)
node4_right = TreeNode(4, None, node1)
node8 = TreeNode(8, TreeNode(13), node4_right)
root = TreeNode(5, node4_left, node8)

target_sum = 22
result = PS(root, target_sum)
result2 = hasPathSum(root, target_sum)
print(result)  
print(result2)