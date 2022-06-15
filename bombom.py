valores=[[10,11,12,13],[14,15,16,17]]
cartas=["A","J","Q","K"]
dom=list(input())
luana=0
edu=0

for i in range(3):
  carta=list(input())
  if carta[1]==dom[1]:
    luana+=valores[1][cartas.index(carta[0])]
  else:
    luana+=valores[0][cartas.index(carta[0])]

for i in range(3):
  carta=list(input())
  if carta[1]==dom[1]:
    edu+=valores[1][cartas.index(carta[0])]
  else:
    edu+=valores[0][cartas.index(carta[0])]   

if luana>edu:
  print("Luana")
elif edu>luana:
  print("Edu")
else:
  print("empate")
