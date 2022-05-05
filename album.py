# nome: Letícia Fonseca
# nível júnior - 2018 - fase 1

N = int(input())
M = int(input())

album = set()           # set() - lista que não permite/ignora itens repetidos
for i in range(M):      # x será pedido m vezes (figurinhas compradas)
    X = int(input())    # input do(s) x
    album.add(X)        # elementos x adicionados ao set album

print(N - len(album))   # len() - indica quantia de elementos em uma lista