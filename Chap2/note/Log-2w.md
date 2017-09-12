## 170827 2wd7

## 今日探索

1. 参加深圳的小伙伴MeetUP。一个感受就是需要更加自信，投入更多的时间到各种代码上，少看多做，多去碰问题，多去踩坑才能再下次踩坑之后快速出坑

---



## 170826 2wd6

## 今日探索

> 花费4小时

1. 继续封装chap2的程序，分离出一个py文件
2. 看同侪的代码和可以分离出另外一个API的文件看卡包继续优化
3. [chap2的笔记](https://github.com/0x0o/Py101-004/blob/master/Chap2/note/README.md)
4. 看完chap2卡包内容
5. 了解Flask,安装virtualenv，了解virtualenv，安装sublime text 插件 Flask Completions；Flask文档 Quitstart

---





## 170825 2wd5

## 今日探索
> #### 花费2小时
1. 脑子有点糊，看代码中
2. 了解了大概的类方法，静态方法，实例方法的区别和使用场景；在类中使用了@staticmethod
3. 使用了@classmethod 和 @staticmethod 进一步封装, 还需要对查询历史，帮助封装
4. 看同学的代码，并提交chap2任务

## 复盘 & 改进

1. 能够使用类来封装代码了
---



## 170824 2wd4

## 今日探索
> #### 花费1小时
1. 对返回的 status_code 进行了判断。判断字典是否存在key：key in d Return True if d has a key key
2. 对查询历史的判断，如果查询list没有数据，那么打印没有查询历史记录，判断list是空，可以用 not list 返回false。;;使用类初步封装，例如fetchWeather和print_histroy，选择使用类方法@classmethod。完成了初步
## 复盘 & 改进
1. 初步优化对类还不够熟悉，需要了解类方法，静态方法和实例方法的区别
2. 需要不断的给自己增加难度才会进步
---



## 170823 2wd3
没有学习

---


## 170822 2wd2

## 今日探索

> 大约花费1小时

1. 安装 Requests，注册心知天气，用实例API请求了下数据，返回JSON，使用 http://tool.oschina.net/codeformat/json 在线工具格式化了下JSON，更加容易看出JSON的结构
2. 完成了基本的可在线查询天气的功能，requests 非常的好用，直接返回 result.json() 就可以获取到json数据。

## 复盘 & 改进
1. 明天优化这个程序


---

## 170821 2wd1

## 今日探索

> 大约花费1.5小时

1. **继承**

```python
# coding=UTF-8
class SchoolMember:
    '''代表任何学校里的成员。'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''告诉我有关'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''代表一位老师。'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age) # Python 不会自动调用基类SchoolMember的构造函数，这里需要子类显示的调用它
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self) # Python 总会从当前的实际类型中寻找方法，这里调用Teacher的tell而不是SchoolMember的
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''代表一位学生。'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# 打印一行空白行
print()

members = [t, s]
for member in members:
    member.tell()
```


```python
output：
(Initialized SchoolMember: Mrs. Shrividya)
(Initialized Teacher: Mrs. Shrividya)
(Initialized SchoolMember: Swaroop)
(Initialized Student: Swaroop)

Name:"Mrs. Shrividya" Age:"40" Salary: "30000"
Name:"Swaroop" Age:"25" Marks: "75"
```



2. 反转字符串
```python
text = 'abc'
print(text[::-1]) # ::为从头到尾切片，-1 为负数步长，将返回翻转过的文本
```

3. 处理异常
**把可能引发异常或错误的语句放在 try 代码快中，将handler放在except 子语句或代码块中**
```python
s = input('Enter somethin -->')
try:
    text = input('Enter something -->')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))
```

4. 抛出异常
**你可以通过 raise 语句来引发一次异常**
```python
try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
# 其他工作能在此处继续正常运行
except EOFError:
    print('Why did you do an EOF on me?')
```


## 复盘 & 改进
1. 今天把 <简明Python教程> 这本书看完了,非常易懂,其实Python就是5分钟能捡起来,一天就能忘记的语言😅
2. 对于基本的语法更加清晰了一些了. 明天开始所有时间都花在 Coding 上,去碰见更多的坑 -> 解决 -> 记录
3. 今天的精神状态不好, 晚上有一个睡眠仪式比较好



## Changelog
2017-08-26 add 2wd6 log