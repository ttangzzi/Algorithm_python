X = int(input())
N = int(input())
result = 0

for _ in range(0, N):
  a, b = map(int,input().split())
  result += a*b

if result == X:
  print("Yes")
else:
  print("No")