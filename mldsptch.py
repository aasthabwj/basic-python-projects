from multipledispatch  import dispatch
@dispatch(int,int)
def product (f,s):
  r = f*s
  print(r)
@dispatch(int,int,int)
def product (f,s,t):
  r = f*s*t
  print(r)
@dispatch(float,float,float)
def product (f,s,t):
  r = f*s*t
  print(r)
product(1.0,324.4,.78)
