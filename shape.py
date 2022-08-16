class Calc1:
  def sqr(self,a):
    return a*a
class Calc2:
  def rect(self,a,b):
    return a*b
class Derived(Calc1,Calc2):
  def tri(self,a,b):
    return a*b*0.5;

d=Derived()
 print(d.sqr(10))
 print(d.rect(20,22))
 print(d.tri(20,22))
