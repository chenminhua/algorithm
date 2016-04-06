"""
https://leetcode.com/problems/reverse-linked-list/
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if  not head.next:
            return head
        pre = head
        cur = pre.next
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        head.next = None
        return pre
         