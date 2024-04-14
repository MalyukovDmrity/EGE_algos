f = open('27A_2735.txt')
n = int(f.readline())
kx = []
ky = []
k = []
for i in range(n):
    x,y = map(int,f.readline().split())
    if x == 0 and y != 0:
        kx += [x]
    if y == 0 and x != 0:
        ky += [y]
    if x != 0 and y != 0:
        k.append(1)
print(len(kx)*len(ky)*len(k))



