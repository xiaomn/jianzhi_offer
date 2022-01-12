# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指
# 向链表中的任意节点或者 null。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
#  
# 
#  示例 4： 
# 
#  输入：head = []
# 输出：[]
# 解释：给定的链表为空（空指针），因此返回 null。
#  
# 
#  
# 
#  提示： 
# 
#  
#  -10000 <= Node.val <= 10000 
#  Node.random 为空（null）或指向链表中的节点。 
#  节点数目不超过 1000 。 
#  
# 
#  
# 
#  注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-
# pointer/ 
# 
#  
#  Related Topics 哈希表 链表 👍 305 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    # method one
    # def copyRandomList(self, head: 'Node') -> 'Node':
    #     dummy = Node(-1)
    #     first, second = head, dummy
    #     while first:
    #         node = Node(first.val)
    #         second.next = node
    #         first = first.next
    #         second = second.next
    #     first, second = head, dummy.next
    #     while first:
    #         temp1, temp2 = head, dummy.next
    #         while first.random and temp1 != first.random:
    #             temp1 = temp1.next
    #             temp2 = temp2.next
    #         if first.random:
    #             second.random = temp2
    #         first = first.next
    #         second = second.next
    #     return dummy.next

    # method two
    # def copyRandomList(self, head: 'Node') -> 'Node':
    #     if not head:
    #         return
    #     dic = {}
    #     cur = head
    #     while cur:
    #         dic[cur] = Node(cur.val)
    #         cur = cur.next
    #     cur = head
    #     while cur:
    #         dic[cur].next = dic.get(cur.next)
    #         dic[cur].random = dic.get(cur.random)
    #         cur = cur.next
    #     return dic[head]

    # method three
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        cur = head
        while cur:
            temp = Node(cur.val)
            temp.next = cur.next
            cur.next = temp
            cur = temp.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur, ans = head.next, head.next
        while cur.next:
            cur.next = cur.next.next
            cur = cur.next
        return ans


# leetcode submit region end(Prohibit modification and deletion)
