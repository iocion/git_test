import sys
def main():
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    mod = 10**9 + 7
    sum_A = 0
    sum_A2 = 0
    for a in A:
        sum_A = (sum_A + a) % mod
        sum_A2 = (sum_A2 + a * a) % mod
    inv2 = pow(2, mod-2, mod) #费马小定理
    social_value = (sum_A * sum_A - sum_A2) % mod
    social_value = (social_value * inv2) % mod
    print(social_value)

if __name__ == "__main__":
    main()