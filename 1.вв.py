# поиск делитей 
def delit(n):
    d = 2
    while d*d <= n:
        if n % d == 0:
            # возвращаем разность макс и мин делителей(кол-во ночей)
            return n//d - d
        d += 1
    return 0

k = 0 #счётчик

# пербор диапазона в обратном порядке
for i in range(800000,10,-1):
    # проверка оканчания 
    if delit(i) % 100 == 98:
        print(i,delit(i))
        k += 1
        if k == 5:
            break
