def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("Moi nhap chuoi: ")
numbers = list(map(int, input_list.split(',')))
list_dao_nguoc = dao_nguoc_list(numbers)
print("List dao nguoc la: ", list_dao_nguoc)