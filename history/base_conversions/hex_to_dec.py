#Créé le 9 Mai 2023
from math import *

hex=["A","B","C","D","E","F"]
dec=[10,11,12,13,14,15]
while True:
  r=input("Entrez la valeur en hexadecimal : ")
  l=len(str(r))
  v=[str(i) for i in str(r)]
  for a in range(l):
    for b in range(6):
      if v[a]==hex[b]:v[a]=dec[b]
  c,m=0,l-1
  for i in range(l):
    c+=int(v[i])*16**m
    m-=1
  print(c)
