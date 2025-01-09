squares = []
for value in range(0,100,5):
    squares.append(value ** 2)
print(squares)
print(sum(squares))
print(len(squares))
print(max(squares))
print(min(squares))

squares1 = [value **2 for value in range(1,10)]
print(squares1)