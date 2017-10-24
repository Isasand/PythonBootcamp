# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:36:08 2017

@author: Isa
"""
#1
for i in ['a', 2, 'c']:
    try:
        print(i**2)
    except TypeError:
        print("There was a type error")
    else:
        print("Success!")
    finally:
        print("All done")
        
#2

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("Can not divide by zero!")
else:
    print("Success!")
finally:
    print("All done!")
   
#3
    
def ask():
    while True:
        try:
            var = int(input("input an integer: "))
        except: 
            print("Looks like you did not input an integer!")
            continue
        else:
            print("thank you, your number squared is: {}".format(var**2))
            break

ask()