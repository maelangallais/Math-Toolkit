#Créé le 9 Mai 2023
from math import *

while True:
  r=int(input("Entrez la valeur en binaire : "))
  l=len(str(r))
  v=[int(i) for i in str(r)]
  c,m=0,l-1
  for i in range(l):
    if v[m]==1:c+=2**i
    m-=1
  print(c)
