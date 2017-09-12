# 创建一个整数变量
types_of_people = 10
# 根据上面的整数变量创建一个字符串变量
x = f"There are {types_of_people} types of people"

# 创建两个字符串变量
binary = "binary"
do_not = "don't"
# 根据两个字符串变量创建字符串
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

# 根据格式打印
print(f"I said: {x}")
print(f"I also said: '{y}'")

# 创建Bool变量
hilarious = False
joke_evaluation = "Isn't that joke so funny?!{}"
print("Isn't that joke so funny?!{}".format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
print(w + e)
