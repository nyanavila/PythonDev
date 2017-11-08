#!/usr/bin/python3
#First test program
#
# 
class Animal (object):
    def __init__(self, age):
      self.age = age
      self.name = None
    def get_age(self):
      return self.age
    def set_age(self, newage):
      self.age = newage 
#count = 0
xx=0
def toBBinn(n):
    xx=0
    num = bin(n)[2:99].strip()
    r = len(num)
    print(num)
    print(r)
    for count in range(r):
      if num[count] == "1":
        xx += 1
        print(xx)

''' def nb_year(p0, percent, aug, p):
    x=0
    t=0
    while( t < p):
      if( t < p0):
        t = p0+((percent/100)*p0)+aug 
        x += 1
      else:
        t = t+((percent/100)*t)+aug
        x += 1 
    return x '''
def nb_year(p0, percent, aug, p):
    x=0
    t=p0
    while( t < p):
        t = t+((percent/100)*t)+aug
        x += 1 
    print(x)
    
def main():
  print ("Hello World!") 

def digital_root(n):
    count = 0
    s=0
    t=n
    u = str(t)
    r= len(u)
    if(r == 1):
        return t
    else:
        for count in range(r):
            f=int(u[count])
            s += f
            t=s
            digital_root(t)
    print (t)
    return t

''' def iq_test(numbers):
    i=1
    o=[]
    s= []
    v=[]
    f = (numbers.split(" "))
    for i in range(len(f)):
        xx=int(f[i])%2
        if(xx == 0):
            s.append(i+1) 
        else:
            o.append(i+1)
    v.append(s)
    v.append(o)
    f=0
    for f in range(len(v)):
        if(i==0):
            break
        else:
             if(len(v[f]) == 1):
            return v[f][0] '''

def divisors(integer):
    s= []
    for i in range(integer):
        if(i == 0 or i == 1):
            continue
        else:
            if((integer%i) == 0):
                s.append(i) 
    print(s)
        
    
def find_it(seq):
    for f in seq:
        if(seq.count(f)%2 != 0):          
            return f
li=[]
def persistence(n):
    s=1
    x=0
    t=[]
    l=0
    u = str(n)
    k=len(u)
    if( k == 1):
        return (len(li))
    else:
        for i in range(len(u)):
            s *= int(u[i]) 
            t.append(s)
        li.append(t)
        persistence(s)
    return (len(li))


alphabetUp = []
def alpha():
    for letter in range(97,123):
        alphabet.append(chr(letter))

def alphaUp():
    for letter in range(65,91):
        alphabetUp.append(chr(letter))
        ord
''' def alphabet_position(text):
    new=[]
    alphabet=[]
    for letter in range(97,123):
        alphabet.append(chr(letter))
    for i in text:
        r=i.lower()
        if r in alphabet:
            new.append(alphabet.index(r)) 
    ss=(str(new).replace(",",""))
    return ss.replace("[","").replace("]",'') '''
def alphabet_position(text):
    print(' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha()))
''' def digital_root(n):
    count = 0
    o=1
    s=0
    t=n
    u = str(t)
    r= len(u)
    if(r == 1):
        return t
    else:
        for count in range(r):
            f=int(u[count])
            s += f
            t=s
            digital_root(t)
    print (t)
    return t '''
# main()
''' nb_year(1500, 5, 100, 5000)
digital_root(606) '''
''' divisors(75)
find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) '''
print(persistence(999))
alphabet_position("The sunset sets at twelve o' clock.")
''' iq_test("2 4 7 8 10")
iq_test("1 2 2") '''
''' Test.assert_equals(nb_year(1500000, 2.5, 10000, 2000000), 10)
Test.assert_equals(nb_year(1500000, 0.25, 1000, 2000000), 94) '''
''' print(toBBinn(1452))
myanimal = Animal(3)
print (myanimal.age)
myanimal.set_age(10)
print(myanimal.get_age()) '''



