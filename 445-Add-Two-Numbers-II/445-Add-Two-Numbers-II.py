# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        You can reverse the lists then add each node, but I prefer to make a new linked list. First we go through the original list and turn them into 
        strings. Then we add them and turn the value to a string. Next we declare head as the start of our new list, and it's value will be the leftmost 
        digit of the added number, num3. Then loop through every value of num3 except the first and create a new node for every value. Then return the head.
        """
        num1, num2 = "", ""
        while l1 != None:
            num1 += str(l1.val)
            l1 = l1.next
        while l2 != None:
            num2 += str(l2.val)
            l2 = l2.next
        num3 = str(int(num1)+int(num2)) # soup of data type conversions
        head = ListNode(int(num3[0]))
        go = head
        for i in range(1, len(num3)):
            go.next = ListNode(int(num3[i]))
            go = go.next
        return head
