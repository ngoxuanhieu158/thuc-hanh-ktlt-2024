# File: main.py

import mymodule

n = int(input("Nhập số lượng phần tử trong danh sách: "))

values = []
for i in range(n):
    value = float(input(f"Nhập giá trị phần tử thứ {i + 1}: "))
    values.append(value)

sorted_values = mymodule.sort_list(values)

max_value = mymodule.find_max(sorted_values)
min_value = mymodule.find_min(sorted_values)

print("Danh sách đã sắp xếp:", sorted_values)
print("Phần tử lớn nhất:", max_value)
print("Phần tử nhỏ nhất:", min_value)
