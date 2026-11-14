#Créé le 20 Décembre 2023

def nearer(a,x1,x2):
  if x1>=x2:b,c=x1,x2
  else:b,c=x2,x1
  m=(b+c)/2
  if a>=m:r=b
  else:r=c
  return r

def further(a,x1,x2):
  if x1>=x2:b,c=x1,x2
  else:b,c=x2,x1
  m=(b+c)/2
  if a>=m:r=c
  else:r=b
  return r

print(nearer(179,90,270))
print(further(179,90,270))
