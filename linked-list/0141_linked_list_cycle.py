from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines whether a singly linked list contains a cycle.

        This implementation uses Floyd’s Tortoise and Hare algorithm:
        - ptr1 moves one step at a time (slow pointer).
        - ptr2 moves two steps at a time (fast pointer).
        If there is a cycle, the two pointers will eventually meet.

        :param head: Head of the linked list
        :return: True if a cycle exists, otherwise False
        """

        # Initialize both pointers at the head
        ptr1 = head
        ptr2 = head

        # Traverse the list while fast pointer can move
        while ptr2 and ptr2.next:
            # Move slow pointer by one step
            ptr1 = ptr1.next

            # Move fast pointer by two steps
            ptr2 = ptr2.next.next

            # If both pointers meet, a cycle exists
            if ptr1 == ptr2:
                return True

        # If traversal finishes without pointers meeting, no cycle exists
        return False

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each node is visited at most once.
        #
        # Space Complexity:
        # O(1) — Only two pointers are used.
        # ---------------------------------------------------------
