f = open('27A_2730.txt')
n = int(f.readline())
k_12 = []
k = []
for i in range(n):
    x = int(f.readline())
    if x % 12 == 0:
        k_12 += [x]
    else:
        k += [x]
k_12.sort()
k.sort()
a = k_12[-4:] + k[-4:]
ans = []
for i in range(len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            for t in range(k+1,len(a)):
                if (a[i] * a[j] * a[k] * a[t]) % 12 == 0:
                    ans.append(a[i]+a[j]+a[k]+a[t])
print(max(ans))


