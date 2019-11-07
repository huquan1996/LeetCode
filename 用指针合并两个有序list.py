# -*- coding:utf-8 -*-
# author:吉祥鸟
# datetime:2019/3/25 0025 下午 11:13
# software: PyCharm
arr1 = [1, 3, 4, 6, 10]
arr2 = [2, 5, 8, 11]
ind = 0
ans = arr1.copy()
for i in range(0, len(arr2)):
    while ind < len(arr1):
        if arr2[i] <= arr1[ind]:
            ans.insert(ind + i, arr2[i])
            break
        else:
            ind += 1
    else:
        ans = ans + arr2[i:]
        break
print(ans)
