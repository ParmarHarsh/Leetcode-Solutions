from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:
        """
        Removes the n-th node from the end of a singly linked list
        and returns the head of the modified list.

        A dummy node is used to simplify edge cases such as removing
        the head node. Two pointers are used with a gap of n nodes
        between them.

        :param head: Head of the linked list
        :param n: The position from the end of the node to remove
        :return: Head of the modified linked list
        """

        # Create a dummy node that points to the head
        dummy = ListNode(0, head)

        # Left pointer starts at dummy
        l = dummy

        # Right pointer starts at head
        r = head

        # Move the right pointer n steps ahead
        while n > 0 and r:
            r = r.next
            n -= 1

        # Move both pointers until the right pointer reaches the end
        while r:
            l = l.next
            r = r.next

        # Remove the target node
        l.next = l.next.next

        # Return the new head (skipping the dummy node)
        return dummy.next

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — The list is traversed at most once.
        #
        # Space Complexity:
        # O(1) — Only constant extra space is used.
        # ---------------------------------------------------------
