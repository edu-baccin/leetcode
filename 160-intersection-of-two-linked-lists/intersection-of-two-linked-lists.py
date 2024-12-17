# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_count(head):
        current = head
        count = 0 

        while current:
            count += 1
            current = current.next
            
        return count

def align_lists_and_find_intersection(d, headA, headB):
    currentA = headA
    currentB = headB

    for i in range(d):
        if currentA is None:
            return None
        currentA = currentA.next

    while currentA and currentB:
        if currentA == currentB:
            return currentA
        currentA = currentA.next
        currentB = currentB.next
        

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = get_count(headA)
        lenB = get_count(headB)
        diff = 0

        if lenA > lenB:
            diff = lenA - lenB
            return align_lists_and_find_intersection(diff, headA, headB)
        else:
            diff = lenB - lenA
            return align_lists_and_find_intersection(diff, headB, headA)
        
        