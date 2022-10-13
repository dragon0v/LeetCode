# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        crt = 0  # 当前组件的长度
        dummy = ListNode(val=-1, next=head)
        while dummy.next != None:
            dummy = dummy.next
            if dummy.val in nums:
                if crt==0:
                    ans += 1
                crt += 1
            else:
                if crt != 0:
                    crt = 0

        return ans