def UCLN(m, n):
    while n != 0:
        m, n = n, m % n
    return m

m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

result_non_recursive = UCLN(m, n)
print("Ước số chung lớn nhất của", m, "và", n, "là:", result_non_recursive)
