#last 5 digits of the fibonacci number
def Last5ofFib(n):
  a=0
  b=0
  c=1
  for i in range(2,n+1):
    a = b
    b = c
    c = (a + b) % 100000
  return c
print(Last5ofFib(99999999))
