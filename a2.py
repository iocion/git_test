def solve(a1, d1, a2, d2, A, D):
 
    det = a1 * d2 - a2 * d1
    if det == 0:
        return [-1]  
    
    x = (A * d2 - a2 * D) //det
    y = (a1 * D - A * d1) //det
    
    if x < 0 or y < 0:
        return [-1]
    
    return [x, y]


def main():
    T = int(input())
    for _ in range(T):
        a1, d1, a2, d2, A, D = map(int, input().split())
        result = solve(a1, d1, a2, d2, A, D)
        print(*result)

if __name__ == "__main__":
    main()