import search_utils  
def main():
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    lst = []
    print(f"Nhập {n} phần tử của danh sách (phải sắp xếp theo thứ tự tăng dần):")
    for i in range(n):
        value = int(input(f"Nhập phần tử thứ {i + 1}: "))
        lst.append(value)
    search_value = int(input("Nhập giá trị cần tìm: "))
    found = search_utils.binary_search(lst, search_value)
    if found:
        print(f"Giá trị {search_value} được tìm thấy trong danh sách.")
    else:
        print(f"Giá trị {search_value} không có trong danh sách.")
if __name__ == "__main__":
    main()
