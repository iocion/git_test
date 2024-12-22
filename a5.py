def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    w = int(data[1])
    k = int(data[2])
    loc = list(map(int, data[3:3+n]))
    h = list(map(int, data[3+n:3+2*n]))

    def check(t):
        if t == 0:
            return False
        delta = [(-h[i] if h[i] % t == 0 else -(-h[i] // t)) for i in range(n)]
        intervals = [(loc[i] - delta[i], loc[i] + delta[i]) for i in range(n)]
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
        j = 0
        count = 0
        for i in range(n):
            while j < len(merged) and merged[j][1] < loc[i]:
                j += 1
            if j == len(merged) or loc[i] < merged[j][0]:
                count += 1
        return count >= k

    t_min = 1
    t_max = 10**18
    while t_min < t_max:
        t_mid = (t_min + t_max) // 2
        if check(t_mid):
            t_max = t_mid
        else:
            t_min = t_mid + 1
    if check(t_min):
        print(t_min)
    else:
        print(-1)


if __name__ == "__main__":
    main()
