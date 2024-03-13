def count_mines_around(arr, x, y):
    count = 0
    for i in range(max(0, x - 1), min(len(arr), x + 2)):
        for j in range(max(0, y - 1), min(len(arr[0]), y + 2)):
            count += arr[i][j]
    return count - arr[x][y]

arr = []
N = int(input("N: "))
for k in range(N):
  min_map = input(":")
  arr.append(list(map(int, min_map.split())))

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            print("*", end=" ")
        else:
            print(count_mines_around(arr, i, j), end=" ")
    print()