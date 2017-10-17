
# coding: utf-8

# In[1]:


# for getting the syntax differences from c++

class Sample(object):
    pass


# In[44]:


x = Sample()
type(x)


# In[45]:


class Circle(object):
    
    # class object attributes
    pi = 3.14
    
    def __init__(self, radius = 1):
        self.radius = radius
    
    def area(self):
        # radius**2 * pi
        return self.radius**2 * Circle.pi
    
    def set_radius(self,new_radius):
        self.radius = new_radius
    
    def get_radius(self):
        return self.radius


# In[46]:


c = Circle(radius=100)
c.set_radius(50)
c.get_radius()


# In[47]:


#inheritance

class Animal(object):
    
    def __init__(self):
        print("Animal Created")
    
    def whoAmI(self):
        print("Animal")
    
    def eat(self):
        print("Eating")


# In[48]:


class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
        
    def whoAmI(self):
        print("Dog")
    
    def bark(self):
        print("Woff")


# In[50]:


d = Dog()
d.whoAmI()
d.eat()


# In[59]:


class Book(object):

    def __init__(self,title,author,pages):
        
        print("A book has been created")
        self.title = title
        self.author = author
        self.pages = pages
    
    # some special methods, build in function in python 
    
    def __str__(self):
        return "Title: %s, Author: %s, Pages: %s " % (self.title,self.author,self.pages)
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book is gone")


# In[62]:


b = Book('Python', 'Jose', 100)

print(str(b))
print(len(b))
del b

