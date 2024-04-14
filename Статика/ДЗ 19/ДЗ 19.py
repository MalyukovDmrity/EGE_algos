f = open('27A_2731.txt')
n = int(f.readline())
kx = []
ky = []
for i in range(n):
    x,y = map(int,f.readline().split())
    if y == 0:
        kx += [x]
    else:
        ky += [abs(y)]
kx.sort()
ky.sort()
a = kx[-1] - kx[0]
h = max(ky)
print(1/2*a*h)

