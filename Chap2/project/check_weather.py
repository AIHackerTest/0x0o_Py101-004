# -*- coding: utf-8 -*-
from utility.weather import print_histroy, print_help, manage_weather_result


def main():
    print("Hello, 欢迎查天气, 请输入你像查看的城市名, 查看帮助请输入 help or h")
    while True:
        input_name = input(">>>")
        if input_name in ['h', 'help']:
            print_help()
        elif input_name in ['quit', 'exit', 'q']:  # 退出查询
            print_histroy()
            exit()
        elif input_name in ['history', 'hist']:
            print_histroy()
        else:
            manage_weather_result(input_name)


if __name__ == '__main__':
    main()
