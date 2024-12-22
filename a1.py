a, b = map(int, input().split()) 
a1 = abs(a - b)
b1 = a + b
print(str(a1) + "<x<" + str(b1))

# for square in map(lambda x: x**2, [1, 2, 3, 4, 5]):
#     print(square,end=' ')