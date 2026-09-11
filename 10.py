rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

sparse_matrix = {}

print("Enter the matrix elements:")

for i in range(rows):
    for j in range(cols):
        value = int(input(f"Element [{i}][{j}]: "))

        
        if value != 0:
            sparse_matrix[(i, j)] = value

print("\nSparse Matrix Dictionary:")
print(sparse_matrix)

print("\nOriginal Matrix:")
for i in range(rows):
    for j in range(cols):
        print(sparse_matrix.get((i, j), 0), end=" ")
    print()

