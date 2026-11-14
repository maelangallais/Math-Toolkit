#Cree le 28 Novembre
from math import *

p=1
def sum(a,b):
  r=0
  for i in range(a,b+1):
    r+=f(i/(1*10**p))
  return r
fp=input("Fonction : ")
def f(x):
  se={'sqrt':sqrt,'x':x,'abs':fabs,'exp':exp,'log':log10,'cos':cos,'sin':sin}
  return eval(fp,se)
a=int(input("Chiffre de depart : "))
b=int(input("Chiffre d'arrivee : "))
p=int(input("Precision(<5) : "))
y=1*10**(-p)*sum(a*10**p,b*10**p)
print(round(y,p))
