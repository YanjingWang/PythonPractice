"""
Lists are one of the most powerful data structures in python. Lists are sequenced data types.  In Python, an empty list is created using list() function. 
They are just like the arrays declared in other languages. But the most powerful thing is that list need not be always homogeneous. 
A single list can contain strings, integers, as well as other objects. Lists can also be used for implementing stacks and queues. Lists are mutable, 
i.e., they can be altered once declared. The elements of list can be accessed using indexing and slicing operations.
"""
### https://www.geeksforgeeks.org/python-lists/
nums = [1,2,3,4,5,6,7,8,9,10]

# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

my_list2 = [n for n in nums]
# print(my_list2)

# for n in nums:
#     n = n*n
#     my_list.append(n)
# print(my_list)

my_list2 = [n*n for n in nums]
# print(my_list2)

"""map and lambda: map runs everything is the list through a certain function and lambda is an anonymous function"""

my_list3 = map(lambda n: n*n, nums)
print(list(my_list3))


# I want  'n' for each 'n' in nums if 'n' is even
# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)
my_list = [n for n in nums if n%2 == 0]
print(my_list)

my_list3 = filter(lambda n: n%2 == 0 , nums)
print(list(my_list3))

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((num,letter))
# print(my_list)
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

# any data type can be zipped
# any data type can apply to comprehensions
names = ['bruce','clark','peter','logan','wade']
heros = ['batman','superman','spiderman','wolverine','deadpool']
print(dict(zip(names,heros)))

# I want a dict{'name': 'hero'} for each name, hero in zip(names, heros)
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heros) if name != 'peter'}
print(my_dict)

# set() is just list with unique value
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set = (n for n in nums)
print(set(my_set))


# generator expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n
my_gen = gen_func(nums)
for i in my_gen:
    print(i)

my_gen = (n*n for n in nums)  # use parenthesis
print(sorted(my_gen))
"""how to print out in vertical way"""

"""
append() method only works for the addition of elements at the end of the List, for the addition of elements at the desired position, insert() method is used. 
Unlike append() which takes only one argument, the insert() method requires two arguments(position, value). 
"""
# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)
 
# Addition of Element at
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List)

"""
extend(), this method is used to add multiple elements at the same time at the end of the list.
"""
# Python program to demonstrate
# Addition of elements in a List
 
# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)
 
# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List)

"""
reverse a list
"""
mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
mylist.reverse()
print(mylist)
"""
remove(), pop() to delete elements from list
"""

"""
Python List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc. 
A list comprehension consists of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element. 
"""
# below list contains square of all
# odd numbers from range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square) #[1,9,25,49,81]

# for understanding, above generation is same as,
odd_square = []
for x in range(1, 11):
    if x % 2 == 1:
        odd_square.append(x**2) 
print(odd_square)



