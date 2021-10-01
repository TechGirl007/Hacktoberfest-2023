#lucky lotto creater 
from random import*
import random

print("Let's Pick Your Lotto Numbers")

x=[]
for i in range (6):
    rnum=randrange(45)
    x.append(rnum)
print(x)
