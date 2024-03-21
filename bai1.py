def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

# Nhập số Fibonacci muốn tính
n = int(input("Nhập số Fibonacci muốn tính: "))

if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    print("Số Fibonacci tương ứng là:", fibonacci_recursion(n))


