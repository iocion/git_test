def a(N, values):
    MOD = 10**9 + 7
    d = 0
    
    for i in range(N):
        for j in range(i + 1, N):
            d += values[i] * values[j]
    

    return d % MOD

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        values = list(map(int, input().split()))
        
        result = a(N, values)
        print(result)

if __name__ == "__main__":
    main()