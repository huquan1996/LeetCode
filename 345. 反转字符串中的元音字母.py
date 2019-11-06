#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   345. 反转字符串中的元音字母.py
@Time    :   2019/11/06 16:17:52
@Author  :   吉祥鸟
@Contact :   jixnhu@qq.com 
'''

"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:
输入: "hello"
输出: "holle"

示例 2:
输入: "leetcode"
输出: "leotcede"

说明:
元音字母不包含字母"y"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
略微有点繁琐

1. 将输入的字符串另存转换为一个列表
2. 获取到全部的元音字母的位置，将其存到一个列表中
3. 调换位置
4. 将列表转换为字符输出
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yuan=["a","e","i","o","u","A","E","I","O","U"]
        s1=list(s)
        num_list=[]
        for zz,i in enumerate(s):
            if i in yuan:
                num_list.append(zz)
        yuan1=0
        yuan2=len(num_list)-1
        while yuan1 < yuan2:
            s1[int(num_list[yuan2])],s1[int(num_list[yuan1])]=s[int(num_list[yuan1])],s[int(num_list[yuan2])]
            yuan1+=1
            yuan2-=1
        return "".join(s1)

if __name__ == "__main__":
    a = "leetcode"
    print(Solution().reverseVowels(a))
