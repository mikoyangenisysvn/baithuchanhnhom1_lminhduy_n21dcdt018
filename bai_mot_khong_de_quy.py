def fibonacci_non_recursion(n):
    fib = [0, 1]
    if n <= 1:
        return fib[n]
    else:
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]

# Nhập số Fibonacci muốn tính
n = int(input("Nhập số Fibonacci muốn tính: "))

if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    print("Số Fibonacci tương ứng là:", fibonacci_non_recursion(n))

