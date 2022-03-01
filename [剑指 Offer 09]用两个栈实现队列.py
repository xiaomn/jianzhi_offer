# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的
# 功能。(若队列中没有元素，deleteHead 操作返回 -1 ) 
# 
#  
# 
#  示例 1： 
# 
#  输入：
# ["CQueue","appendTail","deleteHead","deleteHead"]
# [[],[3],[],[]]
# 输出：[null,null,3,-1]
#  
# 
#  示例 2： 
# 
#  输入：
# ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
# [[],[],[5],[2],[],[]]
# 输出：[null,-1,null,null,5,2]
#  
# 
#  提示： 
# 
#  
#  1 <= values <= 10000 
#  最多会对 appendTail、deleteHead 进行 10000 次调用 
#  
#  Related Topics 栈 设计 队列 👍 394 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class CQueue:

    def __init__(self):
        # 用来保存插入的数据
        self.stack_add = []
        # 用来保存要删除的数据
        self.stack_delete = []

    def appendTail(self, value: int) -> None:
        # 直接插入到栈的尾部
        self.stack_add.append(value)

    def deleteHead(self) -> int:
        # 如果保存要删除的数据的栈空了，就先把另一个栈的数据出栈同时插入到这个栈中，此时栈里面的数据经过两次后进先出就变成先进先出了
        if not self.stack_delete:
            while self.stack_add:
                self.stack_delete.append(self.stack_add.pop())
        if not self.stack_delete:
            return -1
        return self.stack_delete.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
# leetcode submit region end(Prohibit modification and deletion)
