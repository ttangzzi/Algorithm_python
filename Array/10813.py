N, M = map(int,input().split())
arr = []
for num in range(N):
  arr.append(num+1)
for index in range(M):
  i,j = map(int, input().split())
  arr[i-1], arr[j-1] = arr[j-1], arr[i-1]
print(*arr)