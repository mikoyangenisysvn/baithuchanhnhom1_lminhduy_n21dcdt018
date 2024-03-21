def tinh_giai_thua(n):
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i
    return giai_thua

def tao_tam_giac_pascal(so_hang):
    tam_giac = []
    for i in range(so_hang):
        hang = []
        for j in range(i + 1):
            hang.append(tinh_giai_thua(i) // (tinh_giai_thua(j) * tinh_giai_thua(i - j)))
        tam_giac.append(hang)
    return tam_giac

def in_tam_giac_pascal(tam_giac):
    for hang in tam_giac:
        print(" ".join(str(s) for s in hang).center(len(tam_giac[-1]) * 3))


so_hang = int(input("Nhập số hàng: "))


tam_giac = tao_tam_giac_pascal(so_hang)
in_tam_giac_pascal(tam_giac)
