f = open('27B_2737.txt')
n = int(f.readline())
k = [0] * n
for i in range(n):
    x = int(f.readline())
    ost = x % 2000
    if x < 2000:
        k[ost] += 1
count = k[1000]*(k[1000]-1)//2
for i in range(1,999+1):
    count += k[i]*k[2000-i]
print(count)
