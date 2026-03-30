# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(float('inf'))
        curr = dummyHead
        while list1 and list2:
            if list1.val <= list2.val:
                node = ListNode(list1.val)
                curr.next = node
                curr = curr.next
                list1 = list1.next if list1.next else None
            else:
                node = ListNode(list2.val)
                curr.next = node
                curr = curr.next
                list2 = list2.next if list2.next else None
        
        if list1:
            while list1:
                node = ListNode(list1.val)
                curr.next = node
                curr = curr.next
                list1 = list1.next if list1.next else None
        
        if list2:
            while list2:
                node = ListNode(list2.val)
                curr.next = node
                curr = curr.next
                list2 = list2.next if list2.next else None
        
        return dummyHead.next