# lib/app.py
print("Hello world!")
# displaying data with print()
print("my name is caroline")
print("what is your name ")
print("have you watched alchemy of souls?!")

# what is your own print() Ending
# say you are writing a full paragraph and dont need a new line character wvery sentence.
# print () can accomodate that end through its optional end parameter
# modify your print() end as follows.
print("Hello World", end=" ")
print("Hello sun!", end="!! ")
print("Hello sky!", end="!!!\n")  
# end can be a string og any length including chracters line the newline \n.
print ("what the hell")

# Exploring python with the python interpreter- to run it run python3 in the terminal


# Numbers.
word = "5"
print(int(word))
# Note that python will convert an integer to a float when performing mah calculations
# for example
divide = 4/3 
print(divide)

# List
# note that list in python is similar to Arrays in javascript 
#  print(type([1,45,37,74545,567363]))

#  Tuples
# Tuples are identical to list with two differences.
# 1. Tuples are created in close parenthesis inplace of square brackets). The tuple() class constructire function can asle be ise to cast lists and other
# iterable data types to tuples.
# example
data =[3,5,6,7,8]
tuple_list= tuple(data)
print(tuple_list)
print(type(tuple_list))
# 2 tupes are immutable.- this means that once a tuple has been created the tuple itself cannot be changed.
# Python function that work on lists to create new data will still work on tuples but tuples do not contain methods like 
# .pop() or .insert() tha would change their contents.
another_data= [76,86,94,32,1,4,65,37]
another_tuple = tuple(another_data)
# new_tuple_list=another_tuple.pop() # this line if code is wrong as tuples do not have methods that work on them.
print(another_tuple)

# Sets and Dicts
# set and dicts in pythons alse store sequences of data, but the individula elements in sets and dicts are unique


# Sets 
# sets are unindexed, unordered and uncheangable.
# thet are initiated with curly braces or the set() class constructor.
# set ()class sonstructr take the list or tuplesas its only argument.
set_constructor= set(another_data)
print(set_constructor)
# set has many methods as the list.


# Dictionaries.
# these dictionaries are equaivalent of javascripts objects.
# they are composed if key/value pairs.Each key points to a specific value, just like a wod and a defination in a regular dictionary.
{key1 :value1, key2:value2, key3:value3}
# to access data from this dictionary , you can use the square brancket notation and pass in the symbol for the key toy are trying to access.
my_dict = {key1 :caroline, key2:wanjiru, key3:selma}
print(my_dict["key2"])
print (my_dict.get("Key3"))

# you can also create dictionaries using the dict()
new_dict = dict(x =1 , y = 4 )

# None
# this is a data type or valut that represent that abesence of a value.
no_value = None
print(no_value)

# Booleans 
# there are only two types of boolean data type True anf False.
# Python as well has the concept of truthy and falsy vlues which when coerced to their equivalnet boolean value, or evaluated as part of a conidtional statement return either True or False
