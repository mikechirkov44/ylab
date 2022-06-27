# Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
# предел (limit), после чего попробуйте сгенерировать по порядку все числа.
# Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL

def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(int(n))
    return primfac


def count_find_num(a, b):
    for i in range(2, b + 1):
        d = primfacs(i)
        if set(a).issubset(set(d)):
            print(i, d)


primesL = [2, 3, 5]
limit = 490

count_find_num(primesL, limit)
