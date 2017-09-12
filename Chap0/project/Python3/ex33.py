

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")

# def loopfun(num):
#     i = 0
#     numbers = []
#     while i < num:
#         numbers.append(i)
#         i = i + 1
#         print("Numbers now: ", numbers)
#         print(f"At the bottom i is {i}")

# loopfun(5)

numbers = []
for i in range(0, 5):
    numbers.append(i)
    print(f"At the bottom i is {i}")
    print("Numbers now:", numbers)
