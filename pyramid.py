# 1. Left-aligned pyramid
print("Left-aligned pyramid:")
for i in range(1, 6):
    print("* " * i)

print("\n2. Right-aligned pyramid:")
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

print("\n3. Full pyramid:")
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

print("\n4. Inverted pyramid:")
for i in range(5, 0, -1):
    print("* " * i)

print("\n5. Number pyramid:")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
