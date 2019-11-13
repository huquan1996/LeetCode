#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   383. 赎金信.py
@Time    :   2019/11/11 08:47:29
@Author  :   吉祥鸟
@GitHub  :   https://github.com/jixn-hu
@CSDN    :   https://me.csdn.net/qq_37462361
'''

"""
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)

注意：

你可以假设两个字符串均只含有小写字母。

    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ransom-note
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # list_ransomNote =list(magazine)
        for i in ransomNote:
            if i not in magazine:
                return False
            magazine = magazine.replace(i,"",1)
        return True

if __name__ == "__main__":
    a=Solution().canConstruct("aa", "ab")
    print(a)
