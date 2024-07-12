def random_number(n):
    result = ""
    i = 1
    while i < n:
        j = i + 1
        while j <= n:
            if n % (i + j) == 0:
                result += str(i) + str(j)
            j += 1
        i += 1
    return result


for n in range(3, 21):
    password = random_number(n)
    print(f"Нужный пароль для числа {n}: {password}")