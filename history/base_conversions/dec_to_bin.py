#Créé le 15 Février 2025

while True:
  r=int(input("Valeur décimale : "))
  buffer=[]
  while r!=0:
   buffer.append(str(r%2))
   r=r//2
  Bin=""
  for string in reversed(buffer):
   Bin+=string
  print(Bin)
