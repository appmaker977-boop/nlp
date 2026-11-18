s = input("Source: ")
t = input("Target: ")

m,n = len(s),len(t)
d = [[0]*(n+1) for i in range(m+1)]

for i in range(m+1):
    d[i][0] = i
for j in range(n+1):
    d[0][j] = j

for i in range(1,m+1):
    for j in range(1,n+1):
        c = 0 if s[i-1] == t[j-1] else 1
        d[i][j] = min(d[i-1][j]+1,
                      d[i][j-1]+1,
                      d[i-1][j-1]+c)

print("Minimum Edit Distance:", d[m][n])