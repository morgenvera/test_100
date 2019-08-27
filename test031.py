'''
实例031：字母识词
题目 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

程序分析 这里用字典的形式直接将对照关系存好。
'''
'Sunday Monday Tuesday Thursday Wednesday Friday Saturday'

weekT = {
    'u':'Tuesday',
    'h':'Thursday'
}

weekS = {
    'u':'Sunday',
    'a':'Saturday'
}

week = {
    'm':'Monday',
    'w':'Wednesday',
    'f':'Friday',
    't': weekT,
    's': weekS
}

a = week[str(input("Please input first character: ")).lower()]
if a == weekS or a == weekT:
    print(a[str(input('Please input second character: ')).lower()])
else:
    print(a)