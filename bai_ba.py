def UCLN(m, n):
    if n == 0:
        return m
    else:
        return UCLN(n, m % n)


m = int(input("Nhập  m: "))
n = int(input("Nhập  n: "))



result_recursive =UCLN(m, n)
print("UCLN", m, "và", n, "là:", result_recursive)
