name = 'zhuzhijie'
age = 26
height = 171
weight = 110
eyes = 'brown'
teeth = 'white'
hair = 'black'

print(f"Let's talk about {name}")  # print("Let's talk about",name)
print(f"He's {height} tall")
print(f"He's {age} old")
print(f"He's {weight} heavy.")


total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

weight = 110

# Kilogram / Pounds Converter.


def kilToPou():
    kilo = int(input("Please enter a value in kilograms to turn it into pounds : "))
    pounds = kilo * 2.2
    print("{0} KH IN POUNDS IS {1}".format(kilo, pounds))

kilToPou()
