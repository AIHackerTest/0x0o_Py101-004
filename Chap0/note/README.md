# Python Cheat Sheet

## List

Make a list
`users = ['val', 'bob', 'mia', 'ron', 'ned']`

Get the first item in a list
`first_user = users[0]`

Get the last item in a list
`newest_user = users[-1]`

Modifying items
`users[0] = 'valerie'`

Adding items to a list
`users.append('amy')`

Starting with an empty list
```Python
users = []
users.append('val')
users.append('bob')
users.append('mia')
users.insert(0, 'joe')
```
Deleting an element by its position
`del users[-1]`

Removing an item by its value
`users.remove('mia')`


popping elements
> If you want to work with an element that you're removing from the list, you can "pop" the element. If you think of the list as a stack of items, pop() takes an item off the top of the stack. By default pop() returns the last element in the list, but you can also pop elements from any position in the list.
```python
most_recent_user = users.pop()
print(most_recent_user)
```

Find the length of a list
```python
num_users = len(users)
print("We have " + str(num_users) + " users.")
```

Sorting a list permanently
`users.sort()`

Sorting a list permanently in reverse alphabetical order
`users.sort(reverse=True)`

Reversing the order of a list
`users.reverse()`

Printing the numbers 0 to 1000
```python
for number in range(1001):
    print(number)
```

计算函数
```python
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
youngest = min(ages)
oldest = max(ages)
total_years = sum(ages)
```


Slicing a list
```python
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]
```

Copying a list
```python
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
copy_of_finishers = finishers[:]
```

## Tuples
```python
Defining a tuple
dimensions = (800, 600)
```

Looping through a tuple
```python
for dimension in dimensions:
    print(dimension)
```

## Dictionaries
```python
Making a dictionary
alien_0 = {'color': 'green', 'points': 5}
```

Getting the value associated with a key
```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
```

Getting the value with get()
```python
alien_0 = {'color': 'green'}
alien_color = alien_0.get('color')
alien_points = alien_0.get('points', 0)
print(alien_color)
print(alien_points)
```

Adding a key-value pair
```python
alien_0 = {'color': 'green', 'points': 5}
alien_0['x'] = 0
alien_0['y'] = 25
alien_0['speed'] = 1.5
```

Modifying values in a dictionary
```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['color'] = 'yellow'
alien_0['points'] = 10
print(alien_0)
```

Deleting a key-value pair
```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
```

Looping through all key-value pairs
```python
fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in fav_languages.items():
    print(name + ": " + language)
```

Looping through all the keys
```python
for name in fav_languages.keys():
    print(name)
```

Looping through all the values
```python
for language in fav_languages.values():
    print(language)
```

Looping through all the keys in order
```python
for name in sorted(fav_languages.keys()):
    print(name + ": " + language)
```

Finding a dictionary's length
```python
num_responses = len(fav_languages)
```

define a list of dictionaries directly,
```python
users = [
    {
        'last': 'fermi',
        'first': 'enrico',
        'username': 'efermi',
    },
    {
    'last': 'curie',
    'first': 'marie',
    'username': 'mcurie',
    },
]

for user_dict in users:
    for k, v in user_dict.items():
        print(k + ": " + v)
        print("\n")
```

字典嵌套List
```python
fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, langs in fav_languages.items():
    print(name + ": ")
    for lang in langs:
        print("- " + lang)
```
