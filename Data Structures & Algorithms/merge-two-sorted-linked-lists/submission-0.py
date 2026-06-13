# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        curr1, curr2 = list1, list2
        dummy = newNode = ListNode()
        while curr1 and curr2:
            if curr1.val < curr2.val:
                newNode.next = curr1
                curr1 = curr1.next
            else:
                newNode.next = curr2
                curr2 = curr2.next
            newNode = newNode.next
        newNode.next = curr1 or curr2
        return dummy.next