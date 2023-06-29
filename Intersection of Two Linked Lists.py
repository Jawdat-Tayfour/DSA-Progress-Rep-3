# My solutin , without watching the explaination, so it might be wrong cuz I'm bad at linked lists, anyways, let's hop on it. 
class ListNode():
    def __init__(self,value=None,next=None):
        self.value = value 
        self.next =  next 
def IOTLL(root_one: ListNode ,root_two: ListNode) -> ListNode : #I know I wasn't sticking to the return type lately 
    curr1 = root_one
    curr2 = root_two
    if not curr1 and not curr2 :
        return None 
    if not curr1 or not curr2:
        return None
    #So we're going to have to pointers and when they match we return the node the match on. 
    if curr1.value == curr2.value :
        return curr1 
    while curr2.next:
        if curr1.value == curr2.value: 
            return curr1
        if not curr1.next and curr2.next:
            curr1 = root_one
            curr2 = curr2.next
        curr1 =curr1.next    
    return None         
# That'll work, Time Complexity O(n+m) where n is the length of the first list and m is the length of the other 
# Space Complexity is O(1). Now let's watch Neet Code's explaination and write his solution. ^_^ . 

# Neet Code Solution
def IOTLL2(headA:ListNode,headB:ListNode):
    l1 , l2 = headA , headB 
    while l1 != l2 :
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA 
    return l1    

# My code just got mocked by my teacher's code. Brilliant 
# Time complexity o(n), Space complexity O(1)


# Create the linked lists
# List 1: 1 -> 2 -> 3 -> 4 -> None
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None 
# List 2: 5 -> 6 -> 3 -> 4 -> None
node5 = ListNode(5)
node6 = ListNode(6)
node5.next = node6
node6.next = node3


# Call the function with the created linked lists
result = IOTLL2(node1, node5)

# Print the result
if result:
    print("Intersection node value:", result.value)
else:
    print("No intersection")

