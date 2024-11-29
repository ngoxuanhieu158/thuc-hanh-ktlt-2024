# File: sort_module.py

def bubble_sort(nlist):
    """Sắp xếp danh sách bằng thuật toán sắp xếp nổi bọt."""
    n = len(nlist)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # So sánh các phần tử cạnh nhau
            if nlist[j] > nlist[j + 1]:
                # Trao đổi chúng
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True
        # Nếu không cần tráo đổi phần tử nào nữa, thoát khỏi vòng lặp
        if not swapped:
            break
    return nlist
