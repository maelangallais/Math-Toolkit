#Créé le 15 Février 2025

HEX=["A","B","C","D","E","F"]
DEC=[10,11,12,13,14,15]

while True:
  r=int(input("Valeur décimale : "))
  buffer,Hex=[],""
  if r==0:Hex+="0"
  while r!=0:
    buffer.append(r%16)
    r=r//16
  for string in reversed(buffer):
    for i in range(6):
      if string==DEC[i]:
        string=HEX[i]
    Hex+=str(string)
  print(Hex)
