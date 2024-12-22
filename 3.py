global_number = 5

def double_global():
    global global_number
    global_number *= 2


double_global()
print(f"全局变量加倍后的值: {global_number}")