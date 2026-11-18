def cyk(s):
    g = {'S': [('A','B')], 'A': ['a'], 'B': ['b']}
    n = len(s)
    t = [[set() for j in range(n)] for i in range(n)]

    for i in range(n):
        for x in g:
            if s[i] in g[x]:
                t[i][i].add(x)

    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            for k in range(i,j):
                for x in g:
                    for a,b in g[x] if x == 'S' else []:
                        if a in t[i][k] and b in t[k+1][j]:
                            t[i][j].add(x)

    return "Accepted" if 'S' in t[0][n-1] else "Rejected"

s = input("Enter string: ")
print(cyk(s))