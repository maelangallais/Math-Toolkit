from math import *

for i in range(1,50):
  if (factorial(i-1)+1)%i==0:
    print(i)
