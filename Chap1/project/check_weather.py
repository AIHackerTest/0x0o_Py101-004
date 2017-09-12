# -*- coding: utf-8 -*-

"""
请在 2wd1 170821 11: 42 前，完成一个最简天气查询程序，运行在命令行界面，实现以下功能：

输入城市名，返回该城市的天气数据；
输入指令，打印帮助文档（一般使用 h 或 help）；
输入指令，退出程序的交互（一般使用 quit 或 exit）；
在退出程序之前，打印查询过的所有城市。
所用天气数据见 https: // github.com/AIHackers/Py101-004/tree/master/Chap1/resource中weather_info.txt 文件。
"""

# 打开，读取，保存到字典中
filename = 'weather_info.txt'
weather_dict = {}

with open(filename) as file_object:
    for line in file_object:
        data_list = line.split(',')
        city = data_list[0]
        weather = data_list[1]
        weather_dict[city] = weather

print("Hello, 欢迎查天气, 请输入你想要查看的城市名, 查看帮助请输入 help or h")

input_city_histroy_list = []


def print_histroy(histroy_list):
    for histroy in histroy_list:
        print(histroy.replace(',', ':'))


def main():
    while True:
        input_name = input(">>> ")
        if input_name in ['h', 'help']:
            print("""
                输入城市名，返回该城市的天气数据；
                输入指令，打印帮助文档（一般使用 h 或 help）；
                输入指令，退出程序的交互（一般使用 quit 或 exit）；
                """)
        elif input_name in weather_dict.keys():
            print(weather_dict[input_name])
            check_history = input_name + ',' + weather_dict[input_name].rstrip('\n')
            input_city_histroy_list.append(check_history)

        elif input_name in ['quit', 'exit', 'q']:
            print("退出查询")
            # 打印查询过的城市
            print("-------------查询过的城市-------------")
            print_histroy(input_city_histroy_list)
            exit()
        elif input_name in ['history', 'hist']:
            print("-------------查询过的城市-------------")
            print_histroy(input_city_histroy_list)
        else:
            print("请查看你的输入是否是一个城市？输入 help or h 查看帮助")


if __name__ == '__main__':
    main()
