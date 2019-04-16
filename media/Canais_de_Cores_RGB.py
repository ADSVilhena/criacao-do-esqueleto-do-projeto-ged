
# coding: utf-8

# In[26]:


import cv2
import matplotlib.pyplot as plt


# In[30]:


img1 = cv2.imread('witcher.jpeg')
RGB = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
rows, cols, channels = RGB.shape

for x in range(cols):
    for y in range(rows):
        RGB.itemset((y,x,0),1)
        RGB.itemset((y,x,1),0)
plt.title('Blue')
plt.imshow(RGB)
plt.show()


# In[68]:


img2 = cv2.imread('dgi.jpeg')
RGB1 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
rows, cols, channels = RGB.shape

for x in range(cols):
    for y in range(rows):
        RGB1.itemset((y,x,0),0)
        RGB1.itemset((y,x,0),254)
plt.title('RED')
plt.imshow(RGB1)
plt.show()


# In[74]:


img3 = cv2.imread('ffxv.jpeg')
RGB2 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
rows, cols, channels = RGB2.shape

for x in range(cols):
    for y in range(rows):
        RGB2.itemset((y,x,0),0)
        RGB2.itemset((y,x,0),0)
plt.title('GREEN')
plt.imshow(RGB2)
plt.show()

