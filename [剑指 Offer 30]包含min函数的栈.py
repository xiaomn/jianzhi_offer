# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。 
# 
#  
# 
#  示例: 
# 
#  MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.min();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.min();   --> 返回 -2.
#  
# 
#  
# 
#  提示： 
# 
#  
#  各函数的调用总次数不超过 20000 次 
#  
# 
#  
# 
#  注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/ 
#  Related Topics 栈 设计 👍 256 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_main = []
        self.stack_auxi = []

    def push(self, x: int) -> None:
        self.stack_main.append(x)
        if not self.stack_auxi or x <= self.stack_auxi[-1]:
            self.stack_auxi.append(x)

    def pop(self) -> None:
        x = self.stack_main.pop()
        if x == self.stack_auxi[-1]:
            self.stack_auxi.pop()

    def top(self) -> int:
        return self.stack_main[-1]

    def min(self) -> int:
        return self.stack_auxi[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
# leetcode submit region end(Prohibit modification and deletion)
