# This is a simple Python program that greets the user and asks for their name.
print ("HELLO Manan")
# Use of Print function to display a message
print("Welcome to the world of Python")
# Input function to take user input
# dummy input just to pause execution, value is discarded
input("ENTER ANY THING FOR INPUT: ")
# USE of input function to take user input and store it in a variable "name".
name = input("Enter your name? ")
print("Hello",name,"! Welcome to the world of Python programming.")
# This hash is use for comment only and will not be executed by the python interpreter.
 
"""                                          
# This comments also use as a documentation for the code and can be used to explain the code to other developers or users.
# This comments also use as a Pseudo code to explain the logic of the code in a simple way or 
# Divide the code into smaller parts for better understanding.
# This Triple DOUBLE QUOTE comments can also be used to create multi-line comments in Python, 
# which can be useful for providing detailed explanations or documentation for the code.
# Inside This """ """ We can write any number of lines of comments or documentation without having to use the hash symbol for each line.
# " <-- This is a QUOTE symbol used to group expressions or statements together in Python. It is also used to define tuples, 
# which are immutable sequences of values.
# Always try to improve your code readability and maintainability by using comments and ,
# documentation to explain the code logic and functionality.
# Python is a case sensitive programming language, which means that it treats uppercase and lowercase letters as different characters.
# Just keep in mind use comments & Make some practice to improve your coding skills and become a better Python developer.
# Python was first developed by GUIDO VAN ROSSUM in the late 1980s and officially released as version 0.9.0 in February 1991.
# Python inventor already code all logic behind the scene, so we can focus on writing the code logic and ,
# functionality without worrying about the low-level details of the programming language.
# For example, Print is function as we know that it is used to display output on the console, 
# but we don't need to know how it works internally or how it is implemented in the Python interpreter. 
# For it details need to go for python documentation or source code to understand the implementation of the print function in Python.
# Like we take print in behind the scene, we saw in documentation 'docs.python.org/3/library/functions.html#print' that it is a,
# built-in function in Python that takes one or more arguments and displays them on the console.
# That print looks like this: 'print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)'
# No need to undersand all in your first time, But we can understand when we cover the advance topics of python programming language.
# These documentation tell us about the parameters which are already defined in python. If we go beyond the parameters, 
# we can see the error in the code.

"""                                           
# This is a two way to print out same output in python, But the first one is more readable and maintainable than the second one.
age = input("Enter your age? ")
print("You are",age,"years old.")       
        # OR
Age =input("Enter your age? ")
print("You are " + Age,"years old.")       
# These are some other way to this in python {This is a new way to do in the python,
# by using f in start and use curly bracket {variable} in this.}. It's a more clean way to right code.
print(f"You are {age} years old.")  

# A curious question? Can we print QUOTE in python? using same print function. 
# Yes, we can print QUOTE in python using print function.
# Some way to print QUOTE in python using print function.
print('HELLO "MANAN"')  # using single quote to print double quote
print("HELLO 'MANAN'")  # using double quote to print single quote

 
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False). Need to understand the parameters of print function in python.
# What does it mean? 
""" 
# This is a PRINT function in python and use-case of them & manipulation.
# In case 1: we can see that first we write some str in place of '*objects' and do change in the sep no space & remove the '\n',
# which means next line also remove from this.Now check output we can understand more.
# Case 2: we change nothing in *objects, just add what we remove i above case. Only change is separator have '?',
# question mark at the place of space Now show the output/result.
# case 3: No changes. Same check the output.
# I use string for better understanding & clarify the concept of print function in python. We can use variable also in place of string. 
# Till now we don't change after 'end='\n''
# Now, If you write file=sys . we need to import sys for activate this function in our current code window.
# file we can write str and in stdout we can write variable & sys need to import a library for support the code
# flush is use to collect the all data and print.
# so, this explain how our print function is work. or  we  can say behind the scenes of print function.
# As, you observe that we can manipulate the parameters of print function in python to get the desired output. 
# We can use different values for the parameters to change the behavior of the print function.
# Library are the pre-written code by python, we just need to import them only.
"""
# use Case of print function according  to documentation.
import sys
str1 = "yes"
str2 = "no"
str3 = "maybe"
print("Flipkart is the best online shopping platform in India.", str1, sep='', end='', file=sys.stdout, flush=False)
print("Amazon is the best online shopping platform in India.", str2, sep='?', end='\n', file=sys.stdout, flush=False)
print("Myntra is the best online shopping platform in India.", str3, sep=' ', end='\n', file=sys.stdout, flush=False)

# STRING IN PYTHON
"""
# string is continuous sequence of characters enclosed in single quotes, double quotes, or triple quotes.
# A bit talk more about the string in python. String is a data type in python that is used to represent text. 
# It is a sequence of characters, which can include letters, numbers, symbols, and whitespace.
# In python, strings are enclosed in either single quotes (' ') or double quotes (" "). For example, 'Hello' and "Hello" are,
# both valid strings in python.
# Strings can also be enclosed in triple quotes (''' ''' or """ """) to create multi-line strings.
# String is a immutable & unicode character in python. It means that once a string is created, 
# it cannot be modified. Any operation that appears to modify a string actually creates a new string.
# immutable means that we cannot change the value of a string after it is created.
# unicode means that strings can represent characters from any language or writing system, 
# including non-Latin scripts such as Mandarin(Chinese). or NAME is assign in unicode in this format 'N=78, A=65, M=77, E=69,'.
# StringsOrre immutaassignedan't be changed after creation) and Unicode-based (can represent any language's characters).
# We can use string methods to manipulate strings,such as concatenation, slicing, and formatting.

 """
