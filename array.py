arr = []
n = int(input("Enter number of elements (max 15): "))
if n > 15:
<<<<<<< HEAD
        print("Too many elements!")
        n = 15
print("Enter elements:")
i = 0
while i < n:
    tmp = int(input(""))
    arr.append(tmp)
    i += 1
print("Array:")
i = 0
while i < n:
    print(arr[i], end=" ")
    i += 1
print("")