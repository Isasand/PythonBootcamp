
# coding: utf-8

# In[49]:


import math

class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        self.distance = math.sqrt((self.coor1[0] - self.coor2[0]) ** 2 + (self.coor1[1] - self.coor2[1]) ** 2) 
        return self.distance
    
    def slope(self):
        self.slope = (self.coor1[1]-self.coor2[1])/(self.coor1[0] - self.coor2[0])
        return self.slope
    


# In[50]:


# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)


# In[51]:


li.distance()


# In[52]:


li.slope()


# In[67]:


class Cylinder(object):
    
    pi = 3.142
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        self.volume = Cylinder.pi * (self.radius ** 2) * self.height
        return self.volume
    
    def surface_area(self):
        self.surface_area = (2 * Cylinder.pi) * self.radius * (self.radius + self.height)
        return self.surface_area
    
    def get_height(self):
        return self.height
    
    def get_radius(self):
        return self.radius
    
    def __del__(self):
        print("A cylinder is gone")


# In[ ]:




