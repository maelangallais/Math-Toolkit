#Créé le 15 Février 2025

HEX=["A","B","C","D","E","F"]
DEC=[10,11,12,13,14,15]

while True:
  r=int(input("Valeur binaire : "))
  iBin=iHex=Hex="";n=0
  for string in reversed(str(r)):
    iBin+=string;n+=1
    if n%4==0 or n==len(str(r)):
      Dec=0
      for i in range(len(iBin)):
        Dec+=int(iBin[i])*2**i
      iBin=""
      cHex=str(Dec)
      for i in range(6):
        if Dec==DEC[i]:cHex=HEX[i]
      iHex+=cHex
  for s in reversed(iHex):Hex+=s
  print(Hex)
