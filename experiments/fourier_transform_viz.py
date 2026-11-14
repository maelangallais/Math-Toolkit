from math import pi,cos,sin,floor,fabs as va,exp
from kandinsky import fill_rect as fr
from time import sleep as sl

n,wh=(0,)*3,(255,)*3
re,gr=(255,0,0),(0,255,0)
ent=lambda n:floor(n)if n-floor(n)<0.5 else floor(n)+1

def animation():
  x,y=cx,cy
  for i in range(4*r*pi):
    fr(0,0,320,222,wh)
    for p in range(i):
      fr(cx+ent(cos(p/(2*r))*r),cy+ent(sin(p/(2*r))*cos(p/(2*r))*r),1,1,n)
    i/=2*r
    adj=cos(i)*r
    opp=sin(i)*cos(i)*r
    x,y=ent(cx+adj),ent(cy+opp)
    fr(x,y,1,1,n)
    dl(cx,cy,x,y,gr)
    sl(.001)

#animation()

def draw_point(cx,cy,cr,cl):
 for rep in range(8*cr*pi):
  adj=cos(rep)*cr
  x=cx+adj
  opp=sin(rep)*cr
  y=cy+opp
  fr(ent(x),ent(y),1,-2*ent(opp),cl)

def dl(x1,y1,x2,y2,cl=n,t=1):
 w=h=1
 dx=min(max((x2-x1)/va(y2-y1)if va(y2-y1)!=0 else x2-x1,-1),1)
 dy=min(max((y2-y1)/va(x2-x1)if va(x2-x1)!=0 else y2-y1,-1),1)
 c=va(x2-x1)if va(x2-x1)>va(y2-y1)else va(y2-y1)
 if va(dx)<va(dy):w,x1,x2=t,x1-(t-1)//2,x2-(t-1)//2
 else:h,y1,y2=t,y1-(t-1)//2,y2-(t-1)//2
 for i in range(c):fr(ent(x1+dx*i),ent(y1+dy*i),w,h,cl)

cx,cy=160,111
fq=[3,5,9]#frequency
tr=4.4#Revolution Time
cps=5#cycles per second
r=100/(len(fq)+1)
step=8*r
nv=2*pi*step*cps*tr#Number of Values

def ft(t):
  ft=len(fq)+.2
  for p in range(len(fq)):
    ft+=cos(t/cps*fq[p])
  return ft

#p=3#precision
#dp=1*10**(-p)
#f1=lambda x:cos(-2*pi*ft(x)*x)
#f2=lambda x:sin(-2*pi*ft(x)*x)
#def sum(fc):
#  sm=0#sum
#  for i in range(tr*10**p+1):
#    sm+=fc(i*dp)
#  return dp*sm
#cgx,cgy=sum(f1),sum(f2)
sx=sy=0

def draw():
  global sx,sy
  for i in range(nv):
    i/=step
    adj=cos(i)*r*ft(i)
    opp=sin(i)*r*ft(i)
    x,y=ent(cx+adj),ent(cy+opp)
    sx,sy=sx+x,sy+y
    fr(x,y,1,1,n)
    #sl(.001)

draw()
fr(160,0,1,222,re)
cgx,cgy=sx/nv,sy/nv
draw_point(cgx,cgy,3,gr)
