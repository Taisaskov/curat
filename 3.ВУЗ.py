# функция, проверяющая простоту
def isp(n):
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
# функция, проверяющая кол-во делитей
def delit(n):
    d = 2
    # счетчик произведения делителей
    k = 1
    # счетчик кол-ва делителей
    m = 0
    while d*d < n:
        if n % d == 0:
            if isp(d):
                k *= d
                m += 1
            if isp(n//d):
                k *= 1
                m += (n//d)
        d += 1
    if d*d == n and isp(d):
        k *= d
        m += 1
    # проверка кол-ва делителей
    if m == 5:
        return k
    else:
        return 0
# перебор значений
for i in range(2,5000+1):
    if delit(i) == i:
        print(i)

        
    
        
            
