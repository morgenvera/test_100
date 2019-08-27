'''
实例037：排序
题目 对10个数进行排序。

程序分析 同实例005。

a = [3, 2, 1]
a.sort()
print(a)
'''

a = []
print("Please input 10 characters: ")
for i in range(10):
    a.append(int(input("")))
a.sort()
print(a)
