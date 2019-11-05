# -*- coding:utf-8 -*-
# author:吉祥鸟
# datetime:2019/6/25 上午7:36
# software: PyCharm


# 冒泡算法升序排列
a = 0  # 这个可以删除的，因为Python赋值的是指针
swap = 0
count = 0
lst = [1, 2, 9, 6,9,66,77,634,96,923, 3]
lst_len = len(lst)
for i in range(lst_len):
    flag = False
    for j in range(lst_len - i - 1):
        count += 1
        if lst[j] < lst[j + 1]:
            a = lst[j]  # 交换方法一
            lst[j] = lst[j + 1]
            lst[j + 1] = a
            # lst[j],lst[j+1] = lst[j+1],lst[j]  # 交换方法二，原理与方法一一样
            swap += 1
            flag = True
    if not flag:
        break
print("排序结果：{}".format(lst))
print("交换次数：{}".format(swap))
print("循环次数：{}".format(count))