k = 119

#случай, когда * - пустота
for i in range(10):
    # составляем нужное нам число с помощью строк
    n = '1' + str(i) + '45780'
    # перевод строки в число для дальнейшего счёта
    n = int(n)
    #проверка на делимотсь
    if n % k == 0: 
        print(n,n//k)
        
#случай, когда * - одна цифра
for i in range(10):
    for j in range(10):
        n = '1' + str(i) + '45' + str(j) +'780' 
        n = int(n)
        if n % k == 0:
            print(n,n//k)

#случай, когда * - две цифры
for i in range(10):
    for j in range(10):
        for z in range(10):
            n = '1' + str(i) + '45' + str(j) + str(z) +'780' 
            n = int(n)
            if n % k == 0:
                print(n,n//k) 
