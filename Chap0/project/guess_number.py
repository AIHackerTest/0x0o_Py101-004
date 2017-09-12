# -*- coding: utf-8 -*-
#
# 程序随机生成一个 20 以内的数字，用户有 10 次机会猜测
# 程序根据用户输入，给予一定提示（大了、小了、正确）
# 猜对或用完 10 次机会，游戏结束
import random


# 第一版本思路：循环10次，正确或者用完10次机会就跳出循环。


random_number = random.randint(1, 20)

print ("请输入   1-20   之内的数字")


def check_number(num):
    try:
        val = int(num)
    except ValueError:
        print("输入数字好吗，人类")


for i in range(1, 11):
    input_number = input("> ")
    check_number(input_number)
    left_chance = 10 - i
    if left_chance == 0:
        print("最后一次你都猜错了")
        break
    if int(input_number) == random_number:
        print("恭喜你猜中了")
        break
    elif int(input_number) > random_number:
        print(f"你猜大了, 还有 {left_chance} 次机会")
    elif int(input_number) < random_number:
        print(f"你猜小了, 还有 {left_chance} 次机会")
