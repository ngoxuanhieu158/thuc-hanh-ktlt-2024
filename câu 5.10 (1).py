# File: main.py

import sort_module

n = int(input("Nhập số lượng phần tử trong danh sách: "))

nlist = []
for i in range(n):
    value = int(input(f"Nhập giá trị phần tử thứ {i + 1}: "))
    nlist.append(value)

sorted_list = sort_module.bubble_sort(nlist)

print("Danh sách sau khi sắp xếp:", sorted_list)
