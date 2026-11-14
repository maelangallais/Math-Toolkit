#Cree le 4 Novembre 2023
from math import *

def f(x,*args):
  r,v=0,list(args)
  n=len(v)
  for i in range(n):r+=v[i]*x**(n-i-1)
  return r
def fl(fp,f): return "f(x)=",fp,"x +",-f

def fn(x,n): return n*x**(n-1)
def fe(x): return e**x
def fp(x,*args):
  r,v=0,list(args)
  n=len(v)-1
  for i in range(n):r+=(n-i)*v[i]*(x**((n-i)-1))
  return r

print("Vous voulez la derivee d'une :")
print("fonction de puissance (1)")
print("fonction exponentielle (2)")
print("fonction polynomiale (3)")
c=int(input())
if c==1:
  x=float(input("\nQuel x ? "))
  n=float(input("Quel puissance ? "))
  print(fn(x,n))
elif c==2:
  x=float(input("\nQuel x ? "))
  print(fe(x))
elif c==3:
  print("\nTu ecris fp(x,a,b...)")
  print("fp(5,3,6,-5)")
