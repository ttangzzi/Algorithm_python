H, M = map(int, input().split())

min = H*60 + M
time = min - 45
H = time // 60
M = time % 60

if 0 <= H <= 23:
  print(H, M)
else:
  print(H+24, M)