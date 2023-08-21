arr = []
for i in range(1, 31):
  arr.append(i)
for i in range(0, 28):
  n = int(input())
  arr.pop(arr.index(n))
print(min(arr))
arr.pop(arr.index(min(arr)))
print(*arr)