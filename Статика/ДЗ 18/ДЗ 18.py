f = open('27A_2738.txt')
n = int(f.readline())
k = [0] * 10
for i in range(n):
    x = int(f.readline())
    els = [int(i) for i in str(x)]
    for j in range(len(els)):
        k[els[j]] += 1
print(min(k))

