import numpy as np
L=12   #length in meters of beam
W=10    #load intensity in kN/m
#Bending moment and shear force at end 1,x=0
x=0
z='The bending moment at x=0 is '
y='The shear force at x=0 is '
Moment=(W*(-6*x**2+6*L*x-L**2))/12
Shear=W* (L/2-x)
print('(a.1)'+z+str(Moment)+' and '+y+str(Shear))

#Bending moment at x=L
x=L
h='The bending moment at x=L is '
v='The shear force at x=L is '
Moment=(W*(-6*x**2+6*L*x-L**2))/12
Shear=W* (L/2-x)
print('a.2.'+h+str(Moment)+' and '+v+str(Shear))


#Question
#When bending moment=0,we get -6*x**2+6*L*x-L**2=0
a=-6
b=6*L
c=-L**2
#By the almighty formula,
discriminant=b**2-4*a*c
rootb1=(-b+np.sqrt(discriminant))/2*a
rootb2=(-b-np.sqrt(discriminant))/2*a
print('b.The points of contraflexure are '+str(rootb2)+ ' and ' +str(rootb1))

#Questionc
#when shear force is 0,
x=L/2
print('c.The point at which shear force is zero is {}'.format(x))


#Questiond
u=0
t=1/100
s=L+t
x=np.arange(u,s,t)
Moment=(W*(-6*x**2+6*L*x-L**2))/12
print('d.Bending moment at each step in the array using the initialized variablr is {}'.format(Moment))

#Questione
Shear=W* (L/2-x)
print('e.Shear force at each step along the span is{}'.format(Shear))

#Questionf
#Let absolute value of bending moment array=BM
#Let Minimum value of bending moment array=miniBM
BM=abs(Moment)
miniBM=min(BM)
#When bending moment is minimum,we get x**2-L*x+(L**2/6)+(2*mBM)/w=0
a=1
b=-L
c=(L**2/6)+(2*miniBM)
#The roots are:
discriminant=b**2-4*a*c
rootf1=(-b+np.sqrt(discriminant))/2*a
rootf2=(-b-np.sqrt(discriminant))/2*a  
print('f.The points along L where absolute values of the bending moment array\
is minimum are {0} and {1}'.format(rootf1,rootf2))


#Questiong
#Let _r_e=relative errors
r_e1=((rootb1-rootf1)/rootb1*100)
r_e2=((rootb2-rootf2)/rootb2*100)
print('g.The relative errors between estimated points of contraflexure are\
      {0}% and {1}%'.format(r_e1,r_e2))

"""
#questionh
#For the maximum
#Let maximum bending moment=mam
"""
mam=max(Moment)
#When bending moment is maximum,x**2-L*x+(L**2/6)+(2*mam)/w=0
a=1
b=-L
c=(L**2/6)+(2*mam)
#The roots are:
discriminant=b**2-4*a*c
rootmax1=(-b+np.sqrt(discriminant))/2*a
rootmax2=(-b-np.sqrt(discriminant))/2*a  
print('h1.The points of maximum bending moment are {0} and {1}'.format(rootmax1,\
rootmax2))
       

#For the minimum
#Let mainimum bending moment=m_
m_=min(Moment)
#When bending moment is minimum,x**2-L*x+(L**2/6)+(2*m_)/w=0
a=1
b=-L
c=(L**2/6)+(2*m_)
#The roots are:
discriminant=b**2-4*a*c
rootmin1=(-b+np.sqrt(discriminant))/2*a
rootmin2=(-b-np.sqrt(discriminant))/2*a 
print('h.2)The minimum bending moment occurs at {0} and {1}'.format(rootmin1,\
rootmin2))                                                         

print('Github:Karis03')



