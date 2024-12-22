import sys


def allocate_prizes(n, k, a):
    prizes = [0] * n

    # 从左到右遍历
    for i in range(1, n):
        if a[i] > a[i - 1]:
            prizes[i] = max(prizes[i], prizes[i - 1] + k)

    # 从右到左遍历
    for i in range(n - 2, -1, -1):
        if a[i] > a[i + 1]:
            prizes[i] = max(prizes[i], prizes[i + 1] + k)

    return prizes


# 读取输入
input = sys.stdin.read
data = input().split()

T = int(data[0])
index = 1

results = []

for _ in range(T):
    n = int(data[index])
    k = int(data[index + 1])
    a = list(map(int, data[index + 2:index + 2 + n]))
    index += 2 + n
    results.append(allocate_prizes(n, k, a))

# 输出结果
for result in results:
    print(" ".join(map(str, result)))
