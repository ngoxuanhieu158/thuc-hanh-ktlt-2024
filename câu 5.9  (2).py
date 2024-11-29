def binary_search(lst, value):
    """
    Tìm kiếm nhị phân trong danh sách đã sắp xếp.
    
    Parameters:
    lst (list): Danh sách các phần tử đã được sắp xếp.
    value (int): Giá trị cần tìm.
    
    Returns:
    bool: True nếu tìm thấy giá trị, False nếu không tìm thấy.
    """
    lower_bound = 0
    upper_bound = len(lst) - 1

    while lower_bound <= upper_bound:
        mid_point = (lower_bound + upper_bound) // 2
        if lst[mid_point] == value:
            return True  
        elif lst[mid_point] < value:
            lower_bound = mid_point + 1  
        else:
            upper_bound = mid_point - 1  
    return False  
