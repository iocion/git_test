def func(lst, a='sum'):
    if a == 'max':
        return max(lst)
    elif a == 'min':
        return min(lst)
    elif a == 'sum':
        return sum(lst)
    else:
        raise ValueError("Invalid parameter 'a'")


numbers = [3, 5, 1, 9, 2]
print(func(numbers, 'max'))  # 返回最大值
print(func(numbers, 'min'))  # 返回最小值
print(func(numbers, 'sum'))  # 返回求和值