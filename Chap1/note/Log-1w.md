
## 170820 1wd7

### 探索记录
> 没有学习


---
## 170819 1wd6

### 探索记录
> 花费1小时
**1. from...import 语法**

使用from ...import 和 import的区别
例如：

```python
import mymodule

mymodule.say_hi()
print('Version', mymodule.__version__)

# from... import...
from mymodule import say_hi, __version__

say_hi()
print('Version', __version__)
```
一个需要模块名加点语法调用。一个不需要
建议还是使用 import 语句，因为不使用可能产生命名冲突
> Python 的一大指导原则是“明了胜过晦涩”
还可以使用 `form mumodule import *`

**2. 面向对象编程**
一个类（Class）能够创建一种新的类型 （Type），其中对象（Object）就是类的实例（Instance）
对象可以使用属于的它的普通变量来存储数据。

- 类的方法: 类的函数叫做类的方法Mothod
- 字段Field: 对象或类的变量
- 字段和方法统称为类的属性Attribute
- 从属于类本身的字段为类变量Class Variables
- 某一类的各个实例或者对象为实例变量Instance Variables

**3. Self**
类方法与普通函数只有一种特定的区别——前者必须有一个额外的名字，这个名字必须添加到参数列表的开头，但是你不用在你调用这个功能时为这个参数赋值，Python 会为它提供。 这种特定的变量引用的是对象本身，按照惯例，它被赋予 self 这一名称

 **4. __init__ 方法**

__init__ 方法会在类的对象被实例化（Instantiated）时立即运行。这一方法可以对任何你想 进行操作的目标对象进行初始化（Initialization）操作。这里你要注意在 init 前后加上的双下划线。

```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# 前面两行同时也能写作
# Person('Swaroop').say_hi()
```


 **5. 类变量与对象变量**

```python
# coding=UTF-8

class Robot:
    """表示有一个带有名字的机器人。"""
    population = 0 # 类变量
    def __init__(self,name):
        self.name = name # 对象变量
        print("(Initializing {}".format(self.name))

        Robot.population += 1 #使用Robot.population而非self.population.还可以用self.__class__.population 使用这个变量
    def die(self):
        """我挂了"""
        print("{} is being destoryed!".format(self.name))

        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候

        没问题，你做得到。"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod # 类方法 (staticmethod(静态方法)) 等同于 how_many = classmethod(how_many)
    def how_many(cls):
        print("We have {:d} robots.".format(cls.population))
droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")

droid1.die()
droid2.die()
Robot.how_many()

# 注意当一个对象变量与一个类变量名称 相同时，类变量将会被隐藏。
#print(Robot.__doc__) #访问文档字符串
```





---
## 170818 1wd5

### 探索记录
看简明Python这本书，花了1.5个小时

1. format() vs str(age)
从其他信息中构建字符串，可以用format(),例如
```python
age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
```
> 使用联立字符串来达到相同的效果：
```python
name + 'is' +str(age) + 'years old'
```
> 但这样实现是很丑陋的，而且也容易出错


2. Python 中 format 方法所做的事情便是将每个参数值替换至格式所在的位置。这之中可以有 更详细的格式，例如：

```python
# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
```

3. 指定结尾不换行
`print('b', end='')`

4. 对象：Python 将程序中的任何内容统称为 对象（Object）。这是一般意义上的说法

### 复盘 & 改进
1. 上面的笔记都是即时记录下来的，可以尝试6-12小时依靠回忆制作 Flashcard



## 170817 1wd4

### 探索记录
> 花费2小时时间

1. 了解 Reading Files 的使用，rstrip() 函数
2. 探究上下文管理器，了解 witth as 语法执行过程
3. 探索 with as 打开文件和普通的打开文件关闭句柄的区别
4. 优化了程序，不再打印\n，加入history搜索

### 复盘 & 改进：
1. 做了笔记 https://github.com/0x0o/Py101-004/blob/master/Chap1/note/note.md
2. 完成卡包任务，要对相关知识点整理成FlashCard，探索课外的知识




---
## 170816 1wd3
### 探索记录
1. 花费1小时完成了chap01 查天气的任务，对filies and exceptions 的操作熟悉了一点

### 复盘 & 改进：
1. 因为昨天晚上非常晚睡觉，导致今天一天都没有精神，所以今天早点睡觉


---
## 1708015 1wd2
### 探索记录
> 一个25分钟倒计时记录一次

- 猜数字游戏尝试：用两个for循环搞不定，其中一个不执行，Google 了下，发现可以用使用内置 enumerate 函数进行遍历，例如这样

```python
for index, item in enumerate(sequence):
    process(index, item)
```

- 猜数字游戏尝试：利用`for i, num in enumerate(random_list):` 判断了A和B的数量，发现一个问题：生成的随机数首位不能为0，起初做法为如果是0那么取出来，用剔除后三位的6个个位数重新生成一个数字，加入到随机List当中。但想想其实如果生成的随机数首位为0，那么重新生成就好了，直到不为0

- 完成猜数字进阶版功能，(range(10)会返回一个0-10的list)

### 复盘 & 改进：
1. 投入的时间还可以再多一点，做完作业可以多看同学们的代码，希望做到像 @thxiami 一样
2. 不用纠结知识点，不需要去主动记忆，Learn by doing，花更多时间Coding，然后优化代码
3. 从卡包里学到的，MVP ~ Minimum Viable Product, 最小可行产品；如果警戒线时间内（如两三个小时）依然没有眉目，及时在课程仓库 Issue 中招呼大伙儿一起解决哦。



---
## 1708014 1wd1
### 探索记录
1. 今天还在做chap0的进阶猜数字游戏。花了1.5小时，做作业过程中利用文档搜索到几个函数，包括list和字符串转换的方法。目前还没有完成

### 复盘：
1.`random_list = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k=4)` random.sample函数直接随机列表
2. `guess_list = list(guess_str)` 直接把guess_str的内容分割成一个 list

### 改进计划：
1. 还是需要更多的倒计时投入到打代码当中