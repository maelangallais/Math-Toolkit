#Créé le 18 Novembre 2023
from math import sqrt
from matplotlib.pyplot import *
from ion import keydown,KEY_OK

print(" ")
print("! N'oublie pas les signes !")
a=float(input("Entrez la valeur de a : "))
b=float(input("Entrez la valeur de b : "))
c=float(input("Entrez la valeur de c : "))

if a>0:sa="+"
else:sa=""
if b>0:sb="+"
else:sb=""
if c>0:sc="+"
else:sc=""

print(" ")
print("f(x)=",sa,a,"x**2",sb,b,"x",sc,c)

print(" ")
print("Forme canonique :")
c2=-a*(((b/a)/2)**2)+c
xs=+(b/a)/2
if (b/a)/2>0:sco="+"
else:sco=""
if c2>0:sc2="+"
else:sc2=""
print(a,"(x",sco,xs,")**2",sc2,c2)

print(" ")
print("Forme factorisee :")
if -c2/a<0:
  print("Il n'y a pas de solution a l'equation.")
  return
elif xs-int(xs)==0 and sqrt(-c2/a)-int(sqrt(-c2/a))==0:
  if xs+sqrt(-c2/a)<0:sco1=""
  else:sco1="+"
  if xs-sqrt(-c2/a)<0:sco2=""
  else:sco2="+"
  print(a,"(x",sco1,xs+sqrt(-c2/a),")")
  print("(x",sco2,xs-sqrt(-c2/a),")")  
elif sqrt(-c2/a)-int(sqrt(-c2/a))==0:
  print(a,"(x",sco,xs,"+",sqrt(-c2/a),")")
  print("(x",sco,xs,"-",sqrt(-c2/a),")")
elif a==1 or -c2/a-int(-c2/a)==0:
  print(a,"(x",sco,xs,"+sqrt(",-c2/a,"))")
  print("(x",sco,xs,"-sqrt(",-c2/a,"))")
else:
  print(a,"(x",sco,xs,"+sqrt(",-c2,"/",a,"))")
  print("(x",sco,xs,"-sqrt(",-c2,"/",a,"))")

print(" ")
print("Les solutions :")
x1=sqrt(-c2/a)-xs
x2=-sqrt(-c2/a)-xs
print("x1 =",x1)
print("x2 =",x2)

print("")
ok=input("La courbe (OK/EXE): ")
scatter(x1,0)
scatter(x2,0)
scatter(-xs,c2)
scatter(0,c)
if x1<x2:
  print("x1<x2")
elif x2<0 and x2<-xs:
  if -xs<x1 and -xs<0:
    arrow(x2,0,-xs-x2,c2)
    if 0<x1:
      arrow(-xs,c2,xs,-(c2-c))
      arrow(0,c,x1,-c)
    elif x1<c:
      arrow(-xs,c2,xs+x1,-c2)
      arrow(x1,0,-x1,c)
  elif 0<-xs:
    arrow(x2,0,-x2,c)
    arrow(0,c,-xs,c2-c)
    arrow(-xs,c2,x1+xs,-c2)
elif 0<x2 and 0<-xs:
  arrow(0,c,x2,-c)
  arrow(x2,0,-xs-x2,c2)
  arrow(-xs,c2,x1+xs,-c2)

if ok=="":
  grid()
  show()
