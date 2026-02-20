from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders a singly linked list in-place to follow the pattern:
        L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

        The algorithm works in three main steps:
        1. Find the middle of the linked list.
        2. Reverse the second half of the list.
        3. Merge the two halves alternately.

        Do not return anything, modify head in-place instead.
        """

        # Step 1: Find the middle of the linked list using slow and fast pointers
        ptr1 = head
        ptr2 = head.next

        while ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next

        # Step 2: Reverse the second half of the list
        ptr3 = ptr1.next

        # Split the list into two halves
        ptr4 = ptr1.next = None

        # Reverse the second half
        while ptr3:
            temp1_ptr = ptr3.next
            ptr3.next = ptr4
            ptr4 = ptr3
            ptr3 = temp1_ptr

        # Step 3: Merge the two halves alternately
        ptr5, ptr3 = head, ptr4

        while ptr3:
            temp2_ptr = ptr5.next
            temp3_ptr = ptr3.next

            ptr5.next = ptr3
            ptr3.next = temp2_ptr

            ptr5 = temp2_ptr
            ptr3 = temp3_ptr

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — The list is traversed a constant number of times.
        #
        # Space Complexity:
        # O(1) — Reordering is done in-place with constant extra space.
        # ---------------------------------------------------------
