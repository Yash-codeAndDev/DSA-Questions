class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        after = head
        before = dummy
        while True:
            cursor = after
            for i in range(k):
                if cursor == None:
                    return dummy.next
                cursor = cursor.next

            curr = after
            prev = before
            for i in range(k):
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode

            after.next = curr
            before.next = prev
            before = after
            after = curr
