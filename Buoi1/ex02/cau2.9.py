
def kt_snt(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
number = int(input("Nhap so can kt: "))
if kt_snt(number):
    print(number, " la snt.")
else:
    print(number, "khong la snt.")