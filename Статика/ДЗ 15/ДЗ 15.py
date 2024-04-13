f = open('27A_2732.txt')
n = int(f.readline())
m = [[] for i in range(80)]
for i in range(n):
    x = int(f.readline())
    ost = x % 80
    m[ost] += [x]
a = []
for i in range(80):
    m[i].sort()
    a+=m[i][:1] + m[i][-1:]
ans = []
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[j]-a[i]) % 80 == 0:
            ans.append(a[j]-a[i])
print(max(ans))
