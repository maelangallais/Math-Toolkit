#Créé le 05 Juin 2025
from math import floor
from kandinsky import fill_rect as fr,get_pixel
from time import sleep as sl

l=[] #List
v=1 #Value
mv=320*222 #Max Value
gr=(0,255,0) #Green
re=(255,0,0) #Red

fr(0,0,320,222,gr)

def gv(v): #Get Value
  l=floor(v/320)
  c=v%320
  return(c,l)

def gp(v): #Get Pixel
  x,y=gv(v)
  return get_pixel(x,y)==gr

while v<=mv/2:
  v+=1
  if gp(v):
    i=2 #Iterator
    while v*i<mv:
      if gp(v*i):
        x,y=gv(v*i)
        fr(x,y,1,1,re)
        sl(0)
      i+=1
    if len(l)<3000:
      l.append(v)
    sl(0)

print(l)
#Difficulté pour afficher
#les valeurs car j'en ai
#3000...

#En plus, pour l'efficacité
#je m'arrête à la moitié.
#Donc après 35520, je n'ai
#plus aucune valeur lue
