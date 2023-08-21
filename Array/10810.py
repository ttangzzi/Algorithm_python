N, M = map(int,input().split())
arr = [0]*N

for _ in range(0, M):
  i, j, k = map(int,input().split())
  for index in range(i-1,j):
    arr[index] = k
for i in range(0, N):
  print(arr[i], end = " ")