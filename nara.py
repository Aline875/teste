lista = [int(i) for i in input().split()]
if lista[0]*lista[1] == lista[2] *lista[3]:
    print(0)
elif lista[0] * lista[1] > lista[2] * lista[3]:
    print(-1)
else:
    print(1)
    