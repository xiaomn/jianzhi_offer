# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "We are happy."
# 输出："We%20are%20happy." 
# 
#  
# 
#  限制： 
# 
#  0 <= s 的长度 <= 10000 
#  Related Topics 字符串 👍 163 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # method one
    # def replaceSpace(self, s: str) -> str:
    #     return s.replace(" ", "%20")

    # method two
    def replaceSpace(self, s: str) -> str:
        ans = []
        for c in s:
            if c == ' ':
                ans.append('%20')
            else:
                ans.append(c)
        return "".join(ans)
# leetcode submit region end(Prohibit modification and deletion)
