# -*- coding: utf-8 -*-

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there's not 10 things in that list, let's fix that.")

# 根据空格来拆分 ten_things 形成数组，赋值给stuff
stuff = ten_things.split(" ")

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()  # The method pop() removes and returns last object or obj from the list.
    print(more_stuff)
    print(f"Adding:{next_one}")
    stuff.append(next_one)

    print(f"There's {stuff} items now.")

print(f"There we go: {stuff}")
print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # 倒数第一个
print(stuff.pop())
# print(f" ".join(stuff))
print(join(" ", stuff))
# The method join() returns a string in which the string elements of sequence have been joined by str separator.
print(f"#".join(stuff[3:5]))
