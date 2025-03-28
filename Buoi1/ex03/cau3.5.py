def dem_so_lan_xh(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_string = input("Nhap danh sach: ")
word_list = input_string.split()

so_lan_xh = dem_so_lan_xh(word_list)
print("So lan xh: ", so_lan_xh)