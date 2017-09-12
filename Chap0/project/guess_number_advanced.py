#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Program name: 猜数字进阶
    Author: 0x0
    Github: https://github.com/0x0o
    Edition：
    Edit date: 2017.08.15
    游戏介绍：程序内部用 0 - 9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942
    用户输入 4 位数进行猜测，程序返回相应提示
    用 A 表示数字和位置都正确，用 B 表示数字正确但位置错误
    用户猜测后，程序返回 A 和 B 的数量
    比如：2A1B 表示用户所猜数字，有 2 个数字，数字、位置都正确，有 1 个数字，数字正确但位置错误
    猜对或用完 10 次机会，游戏结束
"""


import random

# 生成 random_list 保存为四个数字元素的 list # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 可以写成 range(10)
random_list = random.sample(range(10), 4)
# 如果首位为零重新生成
while random_list[0] == 0: 
    random_list = random.sample(range(10), 4)
print("生成的随机数为 {}".format(random_list))

# 用户输入，把输入拆成一个 list
print("请输入 4 位数进行猜测 ")

# 判断用户输入
def check_guess(input_list):
    a = 0
    b = 0
    for i, num in enumerate(random_list):
        if int(guess_list[i]) == int(random_list[i]):  # 数字正确且位置正确
            a += 1
            if a == 4:
                print("恭喜你全部猜中")
                return True
        elif int(guess_list[i]) in random_list:  # 位置正确
            b += 1
    if(a != 4):
        print("{}A{}B".format(a, b))
        return False


chance = 10
for i in range(0,10):
    # 处理用户输入
    guess_num = input("> ")
    guess_list = list(guess_num)
    guess = check_guess(guess_list)
    if chance == 0:
        print("用完 10 次机会，游戏结束")
        break
    if guess:
        break
    else:
        chance -= 1
        print("你还有 {} 次机会".format(chance))




