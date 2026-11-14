#Créé le 3 Mars 2023
from time import *

def mark():
  print("Ce code va mettre ta note sur 20.")
  e=int(input("Combien de notes as-tu à entrer ? "))
  k=0
  for j in range(e):
    k += 1
    a=float(input("Entre ta note " + str(k) + " : "))
    b=float(input("Sur combien est cette note ? "))
    note = a/b*20
    print("Ta note sur vingt est :", note)
  sleep(5)
  instructions()

def average():
  print("Ce code te dira ta moyenne.")
  c=int(input("Combien de notes as-tu à entrer ? "))
  somme=0
  f=0
  for i in range(c):
    f += 1
    moyenne=float(input("Entrez la note " + str(f) +" : "))
    somme += moyenne
  resultat = somme/c
  print("La moyenne est :", resultat)
  sleep(5)
  instructions()

def moyenne():
  print("Ce code te donnera ta moyenne sur 20.")
  d=int(input("Combien de notes as-tu à entrer ? "))
  some=0
  total=0
  g=0
  for h in range(d):
    g += 1
    moyen=float(input("Entrez la note " + str(g) + " : "))
    some += moyen
    sur_vingt=float(input("Entrez sur combien est cette note : "))
    total += sur_vingt
  resultat = some/total*20
  print("La moyenne est :", resultat, "/20")
  sleep(5)
  instructions()

def instructions():
  print(" ")
  print(" ")
  print("Il y a 3 fonctions que tu peux tester : ")
  print("- La première va mettre ta note sur 20")
  print("  si elle ne l'est pas.")
  print("     Il te suffit de taper 1.")
  print("- La deuxième te donnera ta moyenne")
  print("  en fonction de tes notes.")
  print("     Il te suffit de taper 2")
  print("- La troisieme te donnera ta moyenne sur 20")
  print("  meme si tes notes sont sur 30 ou meme 10.")
  print("     Il te suffit de taper 3")
  print("Entrez le nom de la fonction")
  fonction=input("à utiliser : ")
  resultat=eval(fonction)
  if resultat==1:
    mark()
  if resultat==2:
    average()
  if resultat==3:
    moyenne()

instructions()
