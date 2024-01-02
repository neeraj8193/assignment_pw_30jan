#!/usr/bin/env python
# coding: utf-8

# In[1]:


#assignment 30 jan


# In[2]:


#q1 


# In[3]:


per=int(input('enter the percentage'))
if(per>90):
    print('A')
elif(per>80 and per<=90):
    print('B')
elif(per>60 and per<=80):
    print('C')
else:
    print('D')


# In[4]:


#q2


# In[5]:


cost_price_of_bike=int(input('enter the cost price of bike '))
if(cost_price_of_bike>100000):
    tax=cost_price_of_bike*0.15
    print(tax,"tax is in per : ",15)
elif(cost_price_of_bike>50000 and cost_price_of_bike<=100000):
    tax=cost_price_of_bike*0.10
    print(tax,'tax in per : ',10)
else:
    tax=cost_price_of_bike*0.05
    print(tax,'tax in per : ',5)


# In[6]:


#q3


# In[7]:


city=input("input the city name :\n 1.Delhi\n2.Agra\n3.Jaipur:\n")
if(city=='Delhi'):
    priint('Red Fort')
elif(city=='Agra'):
    print('Taj Mahal')
elif(city=='Jaipur'):
    print('Jal Mahal')
else:
    print('input valid city')


# In[8]:


#q4


# In[18]:


number=int(input('enter a number'))
c=0
while(number%3==0):
    c=c+1
    if(number<=10):
        print(c)
    number=number/3
print(c)


# In[19]:


#q5


#  #while loop is used to run a block code until a certain condition is met
#     A while loop is a control flow statement which allows code to be executed repeatedly, depending on whether a condition is satisfied or not. As long as some condition is true, 'while' repeats everything inside the loop block. It stops executing the block if and only if the condition fails.
#     

# In[20]:


n=int(input('enter a number'))
while(n>0):
    print(n)
    n=n-1
    


# In[21]:


#q6


# In[37]:


j=0
n=1
while(n<5):
    while(j<=n):
        print("*")
        j=j+1
    n=n+1


# In[35]:


j=0
n=1
while(n<5):
    while(j<=n):
        print(j*"*")
        j=j+1
    n=n+1


# In[40]:


j,n=1,1
while(n<8):
    print(2*n*"*")
    while(j<n):
        print("*")
        j=j+1
    print(2*n*"*")
    n=n+1


# In[41]:


#q7


# In[42]:


n=10
while(n>0):
    print(n)
    n=n-1


# In[43]:


#q8


# In[44]:


n=1
while(n<=10):
    print(n)
    n=n+1


# In[ ]:




