#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   387. 字符串中的第一个唯一字符.py
@Time    :   2019/11/12 08:25:25
@Author  :   吉祥鸟
@GitHub  :   https://github.com/jixn-hu
@CSDN    :   https://me.csdn.net/qq_37462361
'''

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

    s = "leetcode"
返回 0.

    s = "loveleetcode",
返回 2.
 

注意事项：您可以假定该字符串只包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections

class Solution1(object):  # 方法一
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for a,i in enumerate(s):
            aa = s.replace(i,"",1)
            if i not in aa:
                return a


class Solution2(object):  # 方法二
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        index=0
        count = collections.Counter(s)
        for i in s:
            if count[i]==1:
                return index
            else:
                index+=1
        return - 1
        

if __name__ == "__main__":
    zz1 = Solution1().firstUniqChar("leetcodel")
    print("方法一：",zz1)
    zz2 = Solution2().firstUniqChar("leetcodel")
    print("方法二：",zz2)
 # 方法二的执行速度是方法一的5倍