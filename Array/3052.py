arr = []
for i in range(0, 10):
  arr.append(int(input())%42)
print(len(set(arr)))