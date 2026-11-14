#Créé le 1 Mai 2023
from math import *

def ent(x):
  if x-floor(x)>0.5:
    x=ceil(x)
    return x
  elif x-floor(x)<=0.5:
    x=floor(x)
    return x

#forme simplifiée qui ne fonctionne que pour x > 0
ent=lambda n:int(n)if n-int(n)<0.5 else int(n)+1

#forme simplifiée qui necessite floor
ent=lambda n:floor(n)if n-floor(n)<0.5 else floor(n)+1

#forme simplifiée qui est de chatGPT et 
#qui est absolument du pur génie...
ent=lambda n:floor(n+0.5)

while True:
  a=float(input("Entrez une valeur : "))
  print(ent(a))
