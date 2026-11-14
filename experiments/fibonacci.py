#Créé le 26 Avril 2023

while True:
  n=int(input("Combien de rep ? "))
  a,b=0,1
  for i in range(n):
    print(a)
    a,b=b,a+b
