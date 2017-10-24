# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:02:11 2017

@author: Isa
"""

try:
    2 + 's'
except TypeError:
    print("There was a type error!")
finally:
    print("Finally this was printed")

try:
    f = open('testfile12332', 'w')
    f.write('Test write this')
except IOError: 
    print("Error in writing to file")
#this will succeed
else: 
    print("File write was a success")
 
#this will not
try: 
    f = open('testfile12343', 'r')
    f.write('test write this')
except IOError:
    print("Error in writing to file")
except: 
    print("There was an error")
else: 
    print("File write was a success")
finally:
    print("Allways execute finally code blocks!")


def askint():
    while True:
        try:
            val = int(input("Please enter an integer:"))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else: 
            print("Correct, that is an integer")
            break
        finally:
            print("Finally block executed!")
       
        print(val)
    
askint()