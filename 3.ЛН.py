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
    k = 0
    while d*d < n:
        if n % d == 0:
            if isp(d):
                k += 1
            if isp(n//d):
                k += 1
        d += 1
    if d*d == n and isp(d):
        k += 1
    return k
m = 0 # счётчик произведний 
K = 10**10
# перебор значений
for i in range(100000,300000+1):
    if delit(i) == 3:
        m += 1
        K = min(K,i)
print(m,K)
        
    
        
            
