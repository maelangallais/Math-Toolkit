#Créé le 15 Février 2025

HEX=["A","B","C","D","E","F"]
DEC=[10,11,12,13,14,15]

while True:
  r=str(input("Valeur héxa : "))
  Dec=0
  Bin=""
  for string in str(r):
    for i in range(6):
      if string==HEX[i]:string=DEC[i]
    Dec+=int(string)
    iBin=""
    while Dec!=0:
      iBin+=str(Dec%2)
      Dec=Dec//2
    if len(iBin)<4:
      for _ in range(4-len(iBin)):
        iBin+="0"
    for i in reversed(iBin):
      if len(Bin)==0 and i=="0":continue
      Bin+=i
  print(Bin)
