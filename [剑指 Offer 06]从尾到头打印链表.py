# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。 
# 
#  
# 
#  示例 1： 
# 
#  输入：head = [1,3,2]
# 输出：[2,3,1] 
# 
#  
# 
#  限制： 
# 
#  0 <= 链表长度 <= 10000 
#  Related Topics 栈 递归 链表 双指针 👍 192 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # method one
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        ans = self.reversePrint(head.next)
        ans.append(head.val)
        return ans

    # method two
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
# leetcode submit region end(Prohibit modification and deletion)
