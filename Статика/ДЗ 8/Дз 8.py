f = open('27B_2733.txt')
n = int(f.readline())
k1 = [0] * 80
k2 = [0] * 80
for i in range(n):
    x = int(f.readline())
    ost = x % 80
    if x > 50000:
        k1[ost] += 1
    else:
        k2[ost] +=1
count = k1[0]*(k1[0]-1)//2 + k1[40]*(k1[40]-1)//2
for i in range(1,39+1):
    count+=k1[i]*k1[80-i]

count += k2[0] * k1[0] + k2[40]*k1[40]
for i in range(1,39+1):
    count+= k2[i]*k1[80-i] + k1[i]*k2[80-i]
print(count)