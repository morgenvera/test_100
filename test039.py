'''
实例039：有序列表插入元素
题目 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

程序分析 首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
'''

sort_list = [1, 10, 100, 1000, 10000]
insert_number = int(input("Please input a integer: "))
sort_list.append(insert_number)
sort_list.sort()
print(sort_list)


