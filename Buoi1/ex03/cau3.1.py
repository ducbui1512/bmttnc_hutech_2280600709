def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 ==0:
            tong += num
    return tong

input_list = input("Nhap danh sach (1, 2, 3,...): ")
numbers = list(map(int, input_list.split(',')))

tong_chan = tinh_tong_so_chan(numbers)
print("Tong cac so chan trong list la: ", tong_chan)