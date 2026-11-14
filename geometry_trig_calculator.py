#Créé le 14 Avril 2023
from math import floor

rep=True
while True:
  print(" ")
  if rep:
    print("Calculs de trigonométrie (1),")
    print("triangle rectangle/Pythagore (2),")
    print("le Théorème de Thalès (3) ou")
    print("les multiples (4) .")
    rep=False
  r=int(input("Choisir 1, 2, 3 ou 4 : "))
  if r==1:
    print("Choisir un calcul de longueur (1)")
    la=int(input("ou d'angle (2) : "))
    if la==1:
      print("Choisir un calcul de cos (1),")
      c=int(input("sin (2) ou tan (3) : "))
      if c==1:
        e=int(input("Vous cherchez l'adj (1) ou l'hyp (2) : "))
        if e==1:
          hyp=float(input("Entrez la longueur de l'hypoténuse : "))
          ang=float(input("Entrez la valeur de l'angle : "))
          adj=hyp*cos(radians(ang))
          print("La longueur de l'adjacent est :",str(round(adj,2)))
        elif e==2:
          adj=float(input("Entrez la valeur de l'adjacent : "))
          ang=float(input("Entrez la valeur de l'angle : "))
          hyp=adj/cos(radians(ang))
          print("La longueur de l'hypoténuse est :",str(round(hyp,2)))
      elif c==2:
        e=int(input("Vous cherchez opp (1) ou hyp (2) : "))
        if e==1:
          hyp=float(input("Entrez la longueur de l'hypoténuse : "))
          ang=float(input("Entrez la valeur de l'angle : "))
          opp=hyp*sin(radians(ang))
          print("La longueur de l'opposé est :",str(round(opp,2)))
        elif e==2:
          opp=float(input("Entrez la valeur de l'opposé : "))
          ang=float(input("Entrez la valeur de l'angle : "))
          hyp=opp/sin(radians(ang))
          print("La longueur de l'hypoténuse est :",str(round(hyp,2)))
      elif c==3:
        e=int(input("Vous cherchez opp (1) ou adj (2) : "))
        if e==1:
          adj=float(input("Entrez la valeur de l'adjacent : "))
          ang=float(input("Entrez la valeur de l'angle : "))
          opp=adj*tan(radians(ang))
          print("La longueur de l'opposé est :",str(round(opp,2)))
        elif e==2:
          opp=float(input("Entrez la valeur de l'opposé : "))
          ang=float(input("Entrez la valeur de l'angle : "))
          adj=opp/tan(radians(ang))
          print("La longueur de l'adjacent est :",str(round(adj,2)))
    elif la==2:
      print("Cherchez-vous un angle à partir du cos (1),")
      c=int(input("du sin (2) ou du tan (3) : "))
      if c==1:
        adj=float(input("Entrez la valeur de l'adjacent : "))
        hyp=float(input("Entrez la longueur de l'hypoténuse : "))
        ang=degrees(acos(adj/hyp))
        print("La valeur de l'angle en degrés est :",str(round(ang,2)))
      elif c==2:
        opp=float(input("Entrez la valeur de l'opposé : "))
        hyp=float(input("Entrez la longueur de l'hypoténuse : "))
        ang=degrees(asin(opp/hyp))
        print("La valeur de l'angle en degrés est :",str(round(ang,2)))
      elif c==3:
        opp=float(input("Entrez la valeur de l'opposé : "))
        adj=float(input("Entrez la valeur de l'adjacent : "))
        ang=degrees(atan(opp/adj))
        print("La valeur de l'angle en degrés est :",str(round(ang,2)))
  elif r==2:
    print("Choisir le théorème (1)")
    d=int(input("ou la réciproque (2) : "))
    if d==1:
      c=int(input("Calculer l'hypoténuse (1) ou un petit côté (2) : "))
      if c==1:
        c1=float(input("Entrez la valeur du 1er côté : "))
        c2=float(input("Entrez la valeur du 2eme côté : "))
        hyp=c1**2+c2**2
        sqrthyp=sqrt(c1**2+c2**2)
        print("L'hypoténuse mesure :",str(round(sqrthyp,2)))
        print("Soit : racine carrée de",str(hyp))
      elif c==2:
        hyp=float(input("Entrez la valeur de l'hypoténuse : "))
        c1=float(input("Entrez la valeur du petit côté : "))
        c2=hyp**2-c1**2
        sqrtc2=sqrt(hyp**2-c1**2)
        print("L'autre petit côté mesure :",str(round(sqrtc2,2)))
        print("Soit : racine carrée de",str(c2))
    if d==2:
      pc1=float(input("Entrez la longueur du 1er petit côté : "))
      pc2=float(input("Entrez la longueur du 2eme petit côté : "))
      hyp=float(input("Entrez la longueur de l'hypoténuse : "))
      part1=pc1**2+pc2**2
      part2=hyp**2
      if part1==part2:
        print("Le triangle est rectangle.")
      else:
        print("Le triangle n'est pas rectangle.")
  elif r==3:
    d=int(input("Choisir le Théorème (1) ou la réciproque (2) : "))
    if d==1:
      print("Entrez la valeur du 1er côté ainsi que celui que sa paire et")
      print("la longueur du côté qui va avec celui que vous cherchez.")
      c1=float(input("Entrez la longueur du 1er petit côté : "))
      c2=float(input("Entrez la longueur de sa paire (grand côté) : "))
      oc=float(input("Entrez la longueur de la paire du côté cherché : "))
      hob=int(input("Vous cherchez le petit (1) ou le grand côté (2) : "))
      if hob==1:
        cc=oc*c1/c2
        print("La longueur du côté cherché est de : ",str(round(cc,2)))
        print("Soit : (",oc,"*",c1,")/",c2)
      elif hob==2:
        cc=oc*c2/c1
        print("La longueur du côté cherché est de : ",str(round(cc,2)))
        print("Soit : (",oc,"*",c2,")/",c1)
    elif d==2:
      pc1=float(input("Entrez la longueur du 1er petit côté : "))
      gc1=float(input("Entrez la longueur du grand côté qui va avec lui : "))
      pc2=float(input("Entrez la longueur du 2eme petit côté : "))
      gc2=float(input("Entrez la longueur du grand côté qui va avec lui : "))
      part1=gc1*pc2
      part2=gc2*pc1
      if part1==part2:
        print("Les droites sont parallèles.")
      else:
        print("Les droites ne sont pas parallèles.")
  elif r==4:
    c=int(input("Entrez une valeur : "))
    if c%2==0:
      print("La valeur est paire.")
    else:
      print("La valeur est impaire.")
    for i in range(floor(c/2)):
      if c%(floor(c/2)-i)==0:
        print("La valeur est multiple de",floor(c/2)-i)
