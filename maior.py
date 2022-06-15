N=int(input())
M=int(input())
S=int(input())
I=[]
total=""

for i in range(N,M+1):
  x=[int(a) for a in str(i)]
  if sum(x) ==S:
    I.append(x)

if I==[]:
  total=-1
else:
  for i in range(len(I[-1])):
    total=total+str(I[-1][i])

int(total)
print(total)
