#Créé le 4 Avril 2023
from matplotlib.pyplot import *

nombre=int(input("Combien de données avez vous a relever ? "))
for i in range(nombre):
  print("Entrez les données n° "+str(i+1)+" : ")
  xy=input("Donnez le x,y de depart : ")
  x,y=xy.split(',')
  x=float(x)
  y=float(y)
  xyarr=input("Donnez le x,y d'arrivée : ")
  xarr,yarr=xyarr.split(',')
  xarrbrut=float(xarr)
  yarrbrut=float(yarr)
  xarr=xarrbrut-x
  yarr=yarrbrut-y
  print("Souhaites-tu des étapes ?")
  stage=int(input("1 pour oui et 2 pour non : "))
  if stage==1:
    xprevious=x
    yprevious=y
    combien=int(input("Combien d'étapes veux-tu ? "))
    for a in range(combien):
      xystep=input("Donnez le x,y de l'étape "+str(a+1)+" : ")
      xstep,ystep=xystep.split(',')
      xstepbrut=float(xstep)
      ystepbrut=float(ystep)
      xstep=float(xstep)-xprevious
      ystep=float(ystep)-yprevious
      if a==combien-1:
        yarrbrut=yarrbrut-ystepbrut
        xarrbrut=xarrbrut-xstepbrut
        arrow(xstepbrut,ystepbrut,xarrbrut,yarrbrut)
        scatter(xarrbrut,yarrbrut)
      arrow(xprevious,yprevious,xstep,ystep)
      scatter(xprevious,yprevious)
      scatter(xstepbrut,ystepbrut)
      xprevious,yprevious=xstepbrut,ystepbrut
  else:
    arrow(x,y,xarr,yarr)
    scatter(x,y)
    scatter(xarrbrut,yarrbrut)
show()
grid()