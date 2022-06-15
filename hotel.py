D=int(input())
A=int(input())
N=int(input())

if N<16:
  print((32-N)*(D+((N-1)*A)))
else:
  print((32-N)*(D+14*A))
