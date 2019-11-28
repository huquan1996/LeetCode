#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   434. 字符串中的单词数.py
@Time    :   2019/11/25 09:05:01
@Author  :   吉祥鸟
@GitHub  :   https://github.com/jixn-hu
@CSDN    :   https://me.csdn.net/qq_37462361
'''


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

if __name__ == "__main__":
    print(Solution().countSegments("Hello, my name is John"))
