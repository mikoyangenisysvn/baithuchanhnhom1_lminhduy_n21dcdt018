def sum_of_divisors(n):
    
    total = 1 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def classify_number(n):
    s = sum_of_divisors(n)
    if s < n:
        return "deficient"
    elif s == n:
        return "perfect"
    else:
        return "abundant"

def number():
    x = int(input("Nhập số nguyên dương x: "))
    y = int(input("Nhập số nguyên dương y (y >= x): "))
    if y < x:
        print("Lỗi: y phải lớn hơn hoặc bằng x.")
        return

    print(f"Phân loại các số từ {x} đến {y}:")
    for num in range(x, y+1):
        classification = classify_number(num)
        print(f"Số {num} là {classification}.")


number()
