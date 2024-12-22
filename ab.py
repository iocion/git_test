def reverse(self):
    return self[::-1]

def test(x,y):
    if int(reverse(x)) + int(reverse(y)) == int(reverse(str(int(x)+int(y)))):
        print(int(x)+int(y))
    else:
        print("NO")
        
    
    
    
    
    
if __name__=='__main__':
    a = int(input())
    for _ in range(a):
        b,c = map(str,input().split())
        test(b,c)
    