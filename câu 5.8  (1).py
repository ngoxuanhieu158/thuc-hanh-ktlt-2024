# File: search_module.py

def sequential_search(dlist, item):
    """Tìm kiếm tuyến tính trong danh sách."""
    for index in range(len(dlist)):
        if dlist[index] == item:
            return True, index  
    return False, -1  
