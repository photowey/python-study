# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file String.py
# @description String
# @author WcJun
# @date 2020/06/20
# ---------------------------------------------


# 会输出换行
print('''
python
java

go
''')

print("======================================")

print("""
python
java

go
""")

print("======================================")

# 手动换行 - 转义字符
print("我要\n换\t行")

print("======================================")

world = "python"

print(world[0])
print(world[1])
print(world[2])
print(world[3])
print(world[4])
print(world[5])

print("======================================")

print(world[-0])
print(world[-1])
print(world[-2])
print(world[-3])
print(world[-4])
print(world[-5])

print("======================================")

# 数组越界
# print(world[6])

# 切片
verse = "床前明月光,疑是地上霜"
# 左闭右开
print(verse[1:3])
print(verse[1:11:2])
print(verse[1:])
print(verse[:5])
print(verse[:])

# 格式化
liLei = "LiLei"
hanMeiMei = "MeiMeiHan"
hru = "How are YOU"
print("{}对{}说,{}!".format(liLei, hanMeiMei, hru))
print(f"{liLei}对{hanMeiMei}说,{hru}!")
