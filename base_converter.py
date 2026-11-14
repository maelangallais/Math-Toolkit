#Créé le 15 Février 2025

HEX=["A","B","C","D","E","F"]
DEC=[10,11,12,13,14,15]

def BinToDec(r):
  l=len(str(r))
  v=[int(i) for i in str(r)]
  c,m=0,l-1
  for i in range(l):
    if v[m]==1:c+=2**i
    m-=1
  return c

def HexToDec(r):
  l=len(str(r))
  v=[str(i) for i in str(r)]
  for a in range(l):
    for b in range(6):
      if v[a]==HEX[b]:v[a]=DEC[b]
  c,m=0,l-1
  for i in range(l):
    c+=int(v[i])*16**m
    m-=1
  return c

def DecToBin(r):
  iBin=[]
  while r!=0:
    iBin.append(str(r%2))
    r=r//2
  c=""
  for string in reversed(iBin):
    c+=string
  return c

def DecToHex(r):
  iHex,c=[],""
  if r==0:c+="0"
  while r!=0:
    iHex.append(r%16)
    r=r//16
  for string in reversed(iHex):
    for i in range(6):
      if string==DEC[i]:string=HEX[i]
    c+=str(string)
  return c

def BinToHex(r):
  c=BinToDec(r)
  c=DecToHex(c)
  return c

def HexToBin(r):
  c=HexToDec(r)
  c=DecToBin(c)
  return c

print("1)  Bin → Déc")
print("2)  Hex → Déc")
print("3)  Déc → Bin")
print("4)  Déc → Hex")
print("5)  Bin → Hex")
print("6)  Hex → Bin")
while True:
  a=int(input("\nChoisissez : "))
  if a==1:
    r=int(input("Valeur binaire : \n"))
    print(BinToDec(r))
  if a==2:
    r=input("Valeur héxadécimale : \n")
    print(HexToDec(r))
  if a==3:
    r=int(input("Valeur décimale : \n"))
    print(DecToBin(r))
  if a==4:
    r=int(input("Valeur décimale : \n"))
    print(DecToHex(r))
  if a==5:
    r=int(input("Valeur binaire : \n"))
    print(BinToHex(r))
  if a==6:
    r=input("Valeur héxadécimale : \n")
    print(HexToBin(r))
