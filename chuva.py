n = int(input())
s = int(input())

soma = 0
resultado = 0
dias = list(map(int, input().split()))
vector = []

for i in range(n):
    for j in range(i, n):
        soma += dias[j]
        if soma == s:
            v = soma + dias[i+1]
            if v == s:
                resultado += 1
            else:
                resultado += 2
            break
        elif soma > s:
            break
    soma = 0
    
print(resultado)
