def giaithua(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def neper(n):
    sum_ak = 0
    for k in range(n + 1):
        ak = 1 / giaithua(k)
        sum_ak += ak
    return sum_ak

# Nhập số nguyên n
n = int(input("Nhập số  n (n >= 0): "))

if n < 0:
    print("Vui lòng nhập số không âm.")
else:
    result = neper(n)
    print("Tổng của các số hạng từ a0 đến a{} là: {:.10f}".format(n, result))

