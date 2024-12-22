def func(var):
    if isinstance(var, (int, float)):
        return var * 2
    elif isinstance(var, str):
        return var[::-1]  #逆序
    elif isinstance(var, list):
        return sum(var)
    else:
        raise ValueError("Unsupported data type")



print(func(10))          
print(func("hello"))     
print(func([1, 2, 3]))   