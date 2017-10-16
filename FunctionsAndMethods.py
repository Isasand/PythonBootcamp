
# coding: utf-8

# In[13]:


#write a function that computes the volume of a sphere given its radius

def vol(rad):
    return (4/3 * 3.14159 * pow(rad,3))


# In[15]:


#write a function that checks wheter a number is in a given range(inclusive of high and low)

def ran_check(num, low, high):
    return num < high and num > low


# In[32]:


#write a Python function that accepts a string and calculate the number of upper
#case letters and lower case letters

def up_low(s):
    up = 0
    low = 0
    for letter in s:
        if letter.isupper():
            up+=1
        elif letter.islower():
            low +=1
    print("No. of Upper case characters: ", up)
    print("No. of Lower case characters: ", low)
    


# In[74]:


#write a function that takes a list and returns a new list with unique elements of 
#the first list 

def unique_list(lst):
    l = []
    for item in lst:
        if lst.count(item) == 1:
             l.append(item) 
    return l


# In[108]:


#write a function to multiply all the numbers in a list 

def multiply(numbers):
    sum = numbers[0]
    for num in numbers:
        sum = sum * num
    return sum


# In[113]:


#write a function that checks wheter a passed string is a palidrome or not

def palindrome(s):
    return s[::-1] == s[0:]


# In[126]:


#Write a function to check wheter a string is a panagram or not 
#note: panagrams are words or sentences containing every letter of the alphabet at least once

import string 

def ispangram(str1, alphabet = string.ascii_lowercase):
    for letter in alphabet:
        if str1.count(letter) == 0:
            return False
    return True    

