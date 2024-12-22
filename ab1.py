import random
n = 0
t = [0]*10
# print(type(x))
for i in range(10):
    for _ in range(10):
        x = ''.join(random.sample(list('123456789'),6))
        if(int(x) > 500000):
            n = n + 1
        print(x,end=' ')
        t[i] = n    
    print()

# for j in t:
#     sum = sum + j
print(f"{(t[9])/10}")
# print(f"输出十次大于的平均为{sum/10}")
    