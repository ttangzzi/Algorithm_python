A, B = map(int, input().split())
C = int(input())
min = B+C

if min >= 60:
  A += min // 60
  B = min % 60
else:
  B = min
  
if 0 <= A <= 23:
  print(A, B)
else:
  print(A-24, B)