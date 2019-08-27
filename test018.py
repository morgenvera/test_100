'''
实例018：复读机相加
题目 求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析 用字符串解决。
'''

a = input("Please input base number: ")
add_iter = int(input("Please input add times: "))
sum = 0

if add_iter == 0:
    sum = int(a)
else:
    for i in range(add_iter):
        add_number = int(a*(i+1))
        #print(add_number)
        sum = sum + add_number

print(sum)


