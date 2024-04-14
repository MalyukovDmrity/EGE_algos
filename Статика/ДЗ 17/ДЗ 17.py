f = open('27A_2736.txt')
n = int(f.readline())
k = [0] * 10
for i in range(n):
    x = int(f.readline())
    el = str(x)
    k[int(el[0])] += 1
k.sort()
print(k[1])
