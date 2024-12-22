def find_max_min(lst):
    if not lst:
        return None, None
    
    max_value = min_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    return max_value, min_value

numbers = [3, 5, 1, 9, 2]
max_val, min_val = find_max_min(numbers)
print(f"最大值: {max_val}, 最小值: {min_val}")
print("test")