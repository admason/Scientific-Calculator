#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Binary Conversion of x as function

x = int(input("Enter Decimal integer: "))
b = int(input("Enter Base: "))


def get_bin(x):
    exponent = [i for i in range(10,-1,-1)]#[3,2,1,0]
    bin = []
    for i in exponent:
        if (x/(b**i))%b<1:
            bin.append('0')
        elif (x/(b**i))%b>0:
            bin.append('1')
    return bin
#print(get_bin(x))
#print( x, "in base ",b,"is:")
print (x, "in base ", b, " is:",''.join(get_bin(x)))


# In[ ]:




