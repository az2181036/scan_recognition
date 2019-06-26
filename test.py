

_r = 57/2
high = 1250
dis = 57 + 14.8
high_dis = round(dis/2*3**(1/2))
x = [[100.3, high]]
for i in range(17):
    x.append([x[-1][0]+dis,high])
y = []

for i in range(16):
    y.append([x[i][0]+dis/2,high-high_dis])
print(y)
