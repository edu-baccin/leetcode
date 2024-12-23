# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current = head
        storage = []

        while current:
            storage.append(current.val)
            current = current.next
        
        current = head
        while storage and current:
            current.val = storage.pop()
            current = current.next

        return head
        