## API 的使用

从心知的API Demo 中找到使用 requests 请求API的函数

```python
result = requests.get(API, params={
            'key': KEY,
            'location': location,
            'language': LANGUAGE,
            'unit': UNIT
        }, timeout=7)
    return result.json()
```

从回调函数中获得 json 数据，保存为字典。剩下的事情就和chap1的代码一样的了

## 类的封装

我想调用方法更加简单，例如需要查询天气，就调用函数为 check_weather，返回天气情况，需要查询历史，调用函数为 check_history,返回历史信息。所以做了如下尝试

使用类，创建 CheckWeather类 把 weather 的查询，历史信息，帮助都放到里面，从外面如何调用方便的角度去思考，我想到的是类方法，而不是实例方法，因为实例方法实例化对象，而类方法不需要。例如像这样

```python
CheckWeather.manage_weather_result(input_name)
```
类调用类方法，根据输入信息，直接输出天气状况

```python
CheckWeather.print_histroy()
CheckWeather.print_help()

```
类调用类方法，打印历史和帮助，直接输出天气状况

在类的外面就可以根据用户的输入调用不同的方法，输出信息即可

## 类的实现
在 CheckWeather 的内部，使用 类变量Class Variables，一个list 为 `input_city_histroy_list = []` 来存放查询记录

## 对比 @classmethod VS @staticmethod

1. 当一个函数逻辑上属于一个类又不依赖与类的属性的时候，可以使用 `@staticmethod`。
2. 使用 @staticmethod 可以避免每次使用的时都会创建一个对象的开销。
3. `@staticmethod` 可以使用类和类的实例调用。但是不依赖于类和类的实例的状态。
4. `classmethod` 是类对象与函数的结合。
5. 可以使用类和类的实例调用，但是都是将类作为隐含参数传递过去。
6. 使用类来调用 `classmethod` 可以避免将类实例化的开销。

> 参考：**[PYTHON中STATICMETHOD和CLASSMETHOD的差异](http://www.wklken.me/posts/2013/12/22/difference-between-staticmethod-and-classmethod-in-python.html)**



## Module
单独创建一个py文件放置这个类，如果在其他地方需要用，直接拷过去就可以了。那么我创建utility文件夹存放这个py文件，通过 `from utility.const_value import *` 引入即可

在看同学的代码的时候，发现还可以创建一个 const_value.py 存放常量，例如 API key，LOCATION，API URL，UNIT等，这样就更加具有封装性