# File: main.py

import search_module

n = int(input("Nhập số lượng phần tử trong danh sách: "))

dlist = []
for i in range(n):
    value = int(input(f"Nhập giá trị phần tử thứ {i + 1}: "))
    dlist.append(value)

item = int(input("Nhập phần tử cần tìm: "))

found, index = search_module.sequential_search(dlist, item)

if found:
    print(f"Phần tử {item} được tìm thấy tại chỉ mục {index}.")
else:
    print(f"Phần tử {item} không được tìm thấy trong danh sách.")
