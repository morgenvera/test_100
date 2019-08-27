'''
实例038：矩阵对角线之和
题目 求一个3*3矩阵主对角线元素之和。

程序分析 无。
'''
result = 0
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(mat)):
    result += mat[i][i]
print(result)