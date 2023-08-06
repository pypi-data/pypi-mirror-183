def add(*k):
  s=0
  for i in k:
    s+=i
  return s
#function to add
def iroot(a):
  x=list(map(int,input('enter 1/2 for sqrt, 1/3 for cube root,1/4 for 4th root etc=').replace('/',' ').split()))
  
  v=x[0]/x[1]
  
  
  return a**v
# function for roots
def prime(a):
 if a>1:
   for i in range(2,a//2+1):
     if a%i==0:
       return 'not prime'
       
   else:
    return 'prime'
 else:
   return 'not prime'
# prime
def armstrong(a):
 
  p=len(str(a))
  s=0
  for i in str(a):
    s+=int(i)**p
  if a==s:
    return 'armstrong'
  else:
    return 'not armstrong'
# disarm
def disarm(a):
  
  p=1
  s=0
  for i in str(a):
    s+=int(i)**p
    p+=1
  if a==s:
    return 'disarm'
  else:
    return 'not disarm'

def strongnumber(a):
  x=0
  for i in range(1,a//2+1):
    if a%i==0:
      x+=i
  if x==a:
    return 'strongnumber'
  else:
    return 'not strong'
#strong
      
def special(a):
  sum=0
  for i in str(a):
    fact=1
    
    for k in range(1,int(i)+1):
      fact*=k
      
    sum+=fact
    
  if sum==a:
    return 'special'
  return'not special'



def emrip(a):
  b=a
  a=str(a)
  a=a[::-1]
  if int(a)!=b:
    if prime(int(a))==prime(b):
      if prime(int(a))=='prime':
        return 'emrip'
      return 'not emrip'
    return 'not emrip'
  return 'not emrip'

def spy(a):
  s=0
  m=1
  for i in str(a):
    m*=int(i)
    s+=int(i)
  if m==s:
    return 'spynumber'
  return 'not spynumber'

def help():
  print('''This module is made by prajil,using it u can find emrip number,spynumber,special number,strong number,disarm number,armstrong ,ith root of a number
        import numberprograms
        numberprograms.(spy(),emrip(),special(),strongnumber(),disarm(),iroot())''')

  

