"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：
先根据ascii编码，将原本字符中的不需要的字符和大写的字母去掉或者替换掉，然后前后进行对比
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_x=""
        for i in s:
            ord_i = ord(i)
            if 97<=ord_i<=122 or 48<=ord_i<=57:
                s_x+=i
            elif 65<=ord_i<=90:
                s_x+=chr(ord_i+32)
        for i in range(len(s_x)):
            if s_x[i]!=s_x[-(i+1)]:
                return False
        return True




if __name__ == "__main__":
    print(Solution().isPalindrome("ksddsf"))

    