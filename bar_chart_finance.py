#Créé le 3 Avril 2023
from matplotlib.pyplot import *

nombre=int(input("Combien de mois avez vous a relever ? "))
for i in range(nombre):
  variable=float(input("Entrez les releves du mois "+str(i+1)+" : "))
  bar(i+1,variable)
  if i>=1:
    arrow(i,previous,1,variable-previous)
  previous=variable
show()
grid()
