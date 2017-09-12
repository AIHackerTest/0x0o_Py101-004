# chap01 笔记


## rstrip() 函数

rstrip() 删除 string 字符串末尾的指定字符（默认为空格）

```python
str = "     this is string example....wow!!!     ";
print(str.rstrip())
str = "88888888this is string example....wow!!!8888888";
print(str.rstrip('8'))
```

## 研究 with as 用法
了解到打开文件可以用 with as 的方式来操作，所以去了解这下这个语句。做如下笔记

```python
# with 语句的语法格式
with context_expression [as target(s)]:
    with-body
```

**上下文管理器是什么**

上下文从语义来讲也是很易懂，又难解释的一个词，大概就是一个一前一后的运行环境，那么在 Python 中，经常将一系列操作放在一个语句块中，当某条件为真，执行这个语句块，当某条件为真，循环执行这个语句块

有时候我们需要在当程序在语句块中运行时保持某种状态，并且在离开语句块后结束这种状态。所以，事实上上下文管理器的任务是代码块执行前准备，代码块执行后收拾。它能够让你的代码可读性更强并且错误更少,上下文管理器的常用于一些资源的操作

> 关于上下文管理器目前的我还没办法完全理解。先研究下 with 语句到底做了什么

Python 提供了 with 语句语法，来构建对资源创建与释放的语法糖，with 还可以很好的处理上下文环境产生的异常

```python
# 使用 with 语句操作文件对象
with open('somefileName') as somefile:
    for line in somefile:
        print line
        # ...more code
```

紧跟 with 后面的语句被求值后，返回对象的 __enter__() 方法被呼叫，这个方法的返回值将被赋值给 as 后面的变量。
当 with 后面的代码全部被执行完后，将调用前面返回对象的 __exit__()方法。

这里使用了 with 语句，不管在处理文件过程中是否发生异常，都能保证 with 语句执行完毕后已经关闭了打开的文件句柄。如果使用传统的 try/finally 范式，则要使用类似如下代码：

```python
# try/finally 方式操作文件对象
somefile = open('somefileName')
try:
    for line in somefile:
        print line
        # ...more code
finally:
    somefile.close()
```
比较起来，使用 with 语句可以减少编码量



####参考：

[浅谈 Python 的 with 语句](https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/)

[python黑魔法---上下文管理器（contextor）](http://www.jianshu.com/p/d53449f9e7e0)


