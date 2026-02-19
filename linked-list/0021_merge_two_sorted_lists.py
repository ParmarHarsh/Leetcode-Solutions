from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merges two sorted singly linked lists into one sorted list.

        A dummy node (`result`) is used to simplify handling of the head.
        The `tail` pointer builds the merged list by always attaching
        the smaller current node from either list1 or list2.

        :param list1: Head of the first sorted linked list
        :param list2: Head of the second sorted linked list
        :return: Head of the merged sorted linked list
        """

        # Dummy node to start the merged list
        result = ListNode()

        # Tail pointer to build the merged list
        tail = result

        # Traverse both lists while neither is empty
        while list1 and list2:
            if list1.val < list2.val:
                # Attach node from list1
                tail.next = list1
                list1 = list1.next
            else:
                # Attach node from list2
                tail.next = list2
                list2 = list2.next

            # Move the tail forward
            tail = tail.next

        # If one of the lists is exhausted, attach the remaining nodes
        if list1 == None and list2 != None:
            tail.next = list2
        elif list1 != None and list2 == None:
            tail.next = list1
        elif list1 == None and list2 == None:
            return None

        # Return the head of the merged list (skip dummy node)
        return result.next

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n + m) — Each node from both lists is processed once.
        #
        # Space Complexity:
        # O(1) — Merging is done in-place using existing nodes.
        # ---------------------------------------------------------
