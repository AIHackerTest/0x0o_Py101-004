from sys import argv
# 这是你将 python 的功能引入你的脚本的方法
# argv 是所谓的“参数变量(argument variable)

# 所谓脚本，就是你写的 .py 程序

#接受参数的脚本。
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

