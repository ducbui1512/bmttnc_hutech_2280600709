def xoa_pt(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = 'b'
result = xoa_pt(my_dict, key_to_delete)
if result:
    print("Phan tu da xoa tu Dictionary: ", my_dict)
else: 
    print("Khong tim thay phan tu can xoa trong Dictionary.")