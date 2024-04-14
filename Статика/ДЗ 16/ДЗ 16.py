f = open('27B_2734.txt')
n = int(f.readline())
k = [0]*46
for i in range(n):
    x = int(f.readline())
    s = 0
    #for i in str(x):
    #   s+= int(i)
    #k[s] += 1
    if x == 0:
        k[0] += 1
    else:
        while x != 0:
            s += x % 10
            x = x // 10
        k[s] += 1
print(max(k))