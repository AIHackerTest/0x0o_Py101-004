# -*- coding: utf-8 -*-
#
# 进入迷宫，选择左右
# 左：遇到大龙，选择打还是发育
# 右边：遇到宝藏，拿还是不拿，拿多少，贪心死亡
from sys import exit


def start_room():
    print("欢迎来到迷宫⛩，选择你想进入的大门,（A/B）")
    choice = input("> ")
    if choice == "A":
        dragon_room()
    elif choice == "B":
        storehouse()


def dragon_room():
    print("欢迎进入打龙关")
    print("在你面前是一直3米高的大龙🐲，战斗值是500 (ps:你的战斗值是250😂)")
    print("你的选择是 \nA: 战斗✊\nB: 猥琐发育💪")
    dragon_room_choice = input("> ")
    if dragon_room_choice == "A":
        print("龙一喷火，你烧焦了,游戏结束")
        exit(0)
    elif dragon_room_choice == "B":
        print("聪明")
        print("你想怎么发育")
        print("A: 吃块饼干")
        print("B: 喝药水")
        study_choice = input("> ")
        if study_choice == "A":
            print("吃吃吃，就知道吃，龙一甩尾，你飞了。游戏结束")
            exit(0)
        elif study_choice == "B":
            print("战斗值升到1000，秒了龙，获得宝藏")


def storehouse():
    print("你来到宝藏关，眼前都是珠宝，你想拿多少？")
    how_much = input("> ")
    print("不管你干什么，这些都不属于你，出去！！！！！")


start_room()

about = 10
