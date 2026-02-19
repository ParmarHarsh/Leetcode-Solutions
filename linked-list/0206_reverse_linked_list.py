from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list in-place.

        This implementation uses an iterative approach with two pointers:
        - ptr1: Tracks the previous node (initially None).
        - ptr2: Tracks the current node being processed.

        :param head: Head node of the linked list
        :return: New head of the reversed linked list
        """

        # Pointer to store the previous node (initially None)
        ptr1 = None

        # Pointer to traverse the list (starts at head)
        ptr2 = head

        # Traverse the linked list
        while ptr2:
            # Temporarily store the next node
            temp_ptr = ptr2.next

            # Reverse the current node's pointer
            ptr2.next = ptr1

            # Move ptr1 and ptr2 one step forward
            ptr1 = ptr2
            ptr2 = temp_ptr

        # ptr1 will be the new head of the reversed list
        return ptr1

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each node is visited exactly once.
        #
        # Space Complexity:
        # O(1) — Reversal is done in-place using constant extra space.
        # ---------------------------------------------------------
