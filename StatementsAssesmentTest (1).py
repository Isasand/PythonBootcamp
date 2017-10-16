
# coding: utf-8

# In[1]:


#use for, split(), and if to create a statement that will print out words that start with s


# In[71]:


st = "Print only the words that start with s in this sentence"


# In[106]:


l = [x for x in st.split(" ") if x[0] == "s"]

print(l)


# In[107]:


#use range() to print all the even numbers from 0 to 10 


# In[194]:


for num in range(0,11,2):
    print(num)


# In[190]:


# Use list comprehension to create a list of all numbers between 1 and 50 that are dividible by 3
listOfNumbers = [x for x in range(0,51) if x % 3 == 0]


# In[191]:


print(listOfNumbers)


# In[114]:


#Go through the string below and if the lenght of a word is even print "even"


# In[115]:


st = "Print every word in this sentence that has an even number of letters"


# In[120]:


l =[x for x in st.split(" ") if (len(x) %2 == 0)]


# In[121]:


print(l)


# In[122]:


#Write a program that prints the integers from 1 to 100. 
#But for multiples of three print "Fizz" instead of the number, 
#and for the multiples of five print "Buzz". 
#For numbers which are multiples of both three and five print "FizzBuzz".


# In[127]:


for num in range(1,101):
    if num % 3 == 0:
        print("Fizz")
    elif num % 4 == 0:
        print("Buzz")
    else:
        print(num)


# In[195]:


#Use List Comprehension to create a list of the first 
#letters of every word in the string below:

st = "Create a list of the first letters of every word in this string"
l = [word[0] for word in st.split(" ")] 
print(l)

