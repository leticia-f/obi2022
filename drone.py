# nome: Letícia Fonseca
# nível júnior - 2017 - fase 1

A = int(input()) # dimensão 1 da caixa
B = int(input()) # dimensão 2 da caixa
C = int(input()) # dimensão 3 da caixa

H = int(input()) # altura da janela
L = int(input()) # largura da janela

# append: adicionar variáveis à lista
caixa = []
caixa.append(A)
caixa.append(B)
caixa.append(C)

janela = []
janela.append(H)
janela.append(L)

# sort: ordenar a lista do menor ao maior número
caixa.sort()
janela.sort()


if (caixa[0] <= janela[0]) and (caixa[1] <= janela[1]):
    print("S")
else:
    print("N")