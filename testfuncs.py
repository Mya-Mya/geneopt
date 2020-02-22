# -*- coding: utf-8 -*-
import numpy

class TestFunc:
  def do(self,x,y):
    pass
  def Xmin(self):
    pass
  def Ymin(self):
    pass
  def Xdomain(self):
    pass
  def Ydomain(self):
    pass

class Ackley(TestFunc):
  def do(self,x,y):
    return -20*numpy.exp(-0.2*(0.5*(x**2+y**2))**0.5)-numpy.exp(0.5*(numpy.cos(6.283*x)+numpy.cos(6.283*y)))+22.718
  def Xmin(self):
    return [0]
  def Ymin(self):
    return [0]
  def Xdomain(self):
    return [-5,5]
  def Ydomain(self):
    return [-5,5]

class Bukin(TestFunc):
  def do(self,x,y):
    return 100*(abs(y-0.01*x**2))**0.5+0.01*abs(x+10)
  def Xmin(self):
    return [-10]
  def Ymin(self):
    return [1]
  def Xdomain(self):
    return [-15,-5]
  def Ydomain(self):
    return [-3,3]

class CrossInTray(TestFunc):
  def do(self,x,y):
    return -0.0001*(abs( numpy.sin(x)*numpy.sin(y)*numpy.exp(abs( 100-((x**2+y**2)**0.5)/3.142 )) )+1)**0.1
  def Xmin(self):
    return [1.349,1.349,-1.349,-1.349]
  def Ymin(self):
    return [-1.349,1.349,1.349,-1.349]
  def Xdomain(self):
    return [-10,10]
  def Ydomain(self):
    return [-10,10]

class DropWave(TestFunc):
  def do(self,x,y):
    return -(1+numpy.cos(12*(x**2+y**2)**0.5))/(0.5*(x**2+y**2)+2)
  def Xmin(self):
    return [0]
  def Ymin(self):
    return [0]
  def Xdomain(self):
    return [-5.12,5.12]
  def Ydomain(self):
    return [-5.12,5.12]

class Eggholder(TestFunc):
  def do(self,x,y):
    return -(y+47)*numpy.sin((abs( x/2+y+47 ))**0.5) -x*numpy.sin((abs( x-y-47 ))**0.5)
  def Xmin(self):
    return [512]
  def Ymin(self):
    return [404.232]
  def Xdomain(self):
    return [-512,512]
  def Ydomain(self):
    return [-512,512]

class HolderTable(TestFunc):
  def do(self,x,y):
    return -abs(numpy.sin(x)*numpy.cos(y)*numpy.exp(abs( 1-0.3183*(x**2+y**2)**0.5 )))
  def Xmin(self):
    return [8.055,-8.055,8.055,-8.055]
  def Ymin(self):
    return [9.665,9.665,-9.665,-9.665]
  def Xdomain(self):
    return [-10,10]
  def Ydomain(self):
    return [-10,10]

class Levi(TestFunc):
  def do(self,x,y):
    return (numpy.sin(9.425*x))**2+(1+(numpy.sin(9.425*y)**2))*(x-1)**2+(1+(numpy.sin(6.283*y)**2))*(y-1)**2
  def Xmin(self):
    return [1]
  def Ymin(self):
    return [1]
  def Xdomain(self):
    return [-10,10]
  def Ydomain(self):
    return [-10,10]

class Schaffer(TestFunc):
  def do(self,x,y):
    return 0.5+(numpy.sin(x**2-y**2)**2-0.5)/(1+0.001*(x**2+y**2))**2
  def Xmin(self):
    return [0]
  def Ymin(self):
    return [0]
  def Xdomain(self):
    return [-100,100]
  def Ydomain(self):
    return [-100,100]

class Himmelblau(TestFunc):
  def do(self,x,y):
    return ((x**2)+y-11)**2+(x+(y**2)-7)**2
  def Xmin(self):
    return [3,-2.81,-3.78,3.58]
  def Ymin(self):
    return [2,3.131312,-3.283186,-1.848126]
  def Xdomain(self):
    return [-6,6]
  def Ydomain(self):
    return [-6,6]

class Beale(TestFunc):
  def do(self,x,y):
    return (1.5-x+x*y)**2+((2.25-x+x*(y**2))**2)+(2.625-x+x*(y**3))**2
  def Xmin(self):
    return [3]
  def Ymin(self):
    return [0.5]
  def Xdomain(self):
    return [-4.5,4.5]
  def Ydomain(self):
    return [-4.5,4.5]

class Booth(TestFunc):
  def do(self,x,y):
    return (x+2*y-7)**2+(2*x+y-5)**2
  def Xmin(self):
    return [1]
  def Ymin(self):
    return [3]
  def Xdomain(self):
    return [-10,10]
  def Ydomain(self):
    return [-10,10]

class Matyas(TestFunc):
  def do(self,x,y):
    return 0.26*(x**2+y**2)-0.48*x*y
  def Xmin(self):
    return [0]
  def Ymin(self):
    return [0]
  def Xdomain(self):
    return [-10,10]
  def Ydomain(self):
    return [-10,10]

class Mccormick(TestFunc):
  def do(self,x,y):
    return numpy.sin(x+y)+(x-y)**2-1.5*x+2.5*y+1
  def Xmin(self):
    return [-0.547]
  def Ymin(self):
    return [-1.547]
  def Xdomain(self):
    return [-1.5,4]
  def Ydomain(self):
    return [-3,4]

class Easom(TestFunc):
  def do(self,x,y):
    return -numpy.cos(x)*numpy.cos(y)*numpy.exp(-((x-3.142)**2+(y-3.142)**2))
  def Xmin(self):
    return [3.142]
  def Ymin(self):
    return [3.142]
  def Xdomain(self):
    return [-100,100]
  def Ydomain(self):
    return [-100,100]

class Bird(TestFunc):
  def do(self,x,y):
    return numpy.sin(x)*numpy.exp((1-numpy.cos(y))**2)+numpy.cos(y)*numpy.exp((1-numpy.sin(x))**2)+(x-y)**2
  def Xmin(self):
    return [-2*3.141]
  def Ymin(self):
    return [2*3.141]
  def Xdomain(self):
    return [-10,10]
  def Ydomain(self):
    return [-10,10]

class Giunta(TestFunc):
  def do(self,x,y):
    a=1.067*x-1
    b=numpy.sin(a)
    c=b+b**2+0.02*numpy.sin(4*a)
    d=1.067*y-1
    e=numpy.sin(d)
    f=b+b**2+0.02*numpy.sin(4*d)
    return 0.6+c+f
  def Xmin(self):
    return [0.467]
  def Ymin(self):
    return [0.467]
  def Xdomain(self):
    return [-1,1]
  def Ydomain(self):
    return [-1,1]

class Alpine2(TestFunc):
  def do(self,x,y):
    return numpy.sin(x)*numpy.sqrt(x)*numpy.sin(y)*numpy.sqrt(y)
  def Xmin(self):
    return [7.917]
  def Ymin(self):
    return [7.917]
  def Xdomain(self):
    return [0,10]
  def Ydomain(self):
    return [0,10]

class Shubert3(TestFunc):
  def do(self,x,y):
    a=numpy.sin(2*x+1)+2*numpy.sin(3*x+2)+3*numpy.sin(4*x+3)+4*numpy.sin(5*x+4)+5*numpy.sin(6*x+5)
    b=numpy.sin(2*y+1)+2*numpy.sin(3*y+2)+3*numpy.sin(4*y+3)+4*numpy.sin(5*y+4)+5*numpy.sin(6*y+5)
    return a+b
  def Xmin(self):
    return [7.917]
  def Ymin(self):
    return [7.917]
  def Xdomain(self):
    return [-10,10]
  def Ydomain(self):
    return [-10,10]

class ThreeHump(TestFunc):
  def do(self,x,y):
    return 2*x**2-1.05*x**4+0.166*x**6+x*y+y**2
  def Xmin(self):
    return [0]
  def Ymin(self):
    return [0]
  def Xdomain(self):
    return [-5,5]
  def Ydomain(self):
    return [-5,5]

class EggCrate(TestFunc):
  def do(self,x,y):
    return x**2+y**2+25*(numpy.sin(x)**2+numpy.sin(y)**2)
  def Xmin(self):
    return [0]
  def Ymin(self):
    return [0]
  def Xdomain(self):
    return [-5,5]
  def Ydomain(self):
    return [-5,5]

class Hosaki(TestFunc):
  def do(self,x,y):
    return numpy.exp(-y)*(1-8*x+7*x**2-2.333*x**3+0.25*x**4)*(y**2)
  def Xmin(self):
    return [4]
  def Ymin(self):
    return [4]
  def Xdomain(self):
    return [-5,5]
  def Ydomain(self):
    return [-5,5]

class Goldsteinumpyrice(TestFunc):
  def do(self,x,y):
    return (1+(19-14*x+(3*x**2)-14*y+6*x*y+3*x**2)*((x+y+1)**2))*(30+((2*x-3*y)**2)*(18-32*x+(12*x**2)+48*y-36*x*y+(27*x**2)))
  def Xmin(self):
    return [0]
  def Ymin(self):
    return [-1]
  def Xdomain(self):
    return [-2,2]
  def Ydomain(self):
    return [-2,2]

class StyblinskiTang(TestFunc):
  def do(self,x,y):
    a=x**4-16*x**2+5*x
    b=y**4-16*y**2+5*y
    return (a+b)/2
  def Xmin(self):
    return [-2.904]
  def Ymin(self):
    return [-2.904]
  def Xdomain(self):
    return [-5,4]
  def Ydomain(self):
    return [-3,4]