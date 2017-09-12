import requests


KEY = 'evor2obaqeo8f9es'  # API key
LOCATION = 'beijing'  # 所查询的位置，可以使用城市拼音、v3 ID、经纬度等
API = 'https://api.seniverse.com/v3/weather/now.json'  # API URL，可替换为其他 URL
UNIT = 'c'  # 单位
LANGUAGE = 'zh-Hans'  # 查询结果的返回语言


"""查询程序
    1. print_histroy：历史记录
    2. fetchWeather：查询天气接口，返回json
    3. manage_weather_result 查询天气信息
    """
input_city_histroy_list = []


def fetchWeather(location):
    result = requests.get(API, params={
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout=7)
    return result.json()


def manage_weather_result(location):
    result_dict = fetchWeather(location)
    if 'status_code' in result_dict:
        print('没有查询数据')
        return None
    else:
        weather = result_dict['results'][0]['now']['text']
        temperature = result_dict['results'][0]['now']['temperature']
        check_history = location + '天气：' + weather + ',' + '温度：' + temperature
        input_city_histroy_list.append(check_history)
        return ("{}天气：{}，温度：{}".format(location, weather, temperature))


def print_help():
    str = ("""
            输入中文城市名，返回该城市的天气数据；
            输入使用 h 或 help 指令，打印帮助文档；
            输入使用 quit 或 exit 或 q 指令，退出程序；
            """)
    return str


def manage_history():
    return input_city_histroy_list
