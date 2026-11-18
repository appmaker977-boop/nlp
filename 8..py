states = ['N', 'V']
start = {'N': 0.6, 'V': 0.4}

trans = {'N': {'N': 0.3, 'V': 0.7},
         'V': {'N': 0.8, 'V': 0.2}}

emit = {'N': {'free': 0.5, 'workers': 0.6},
        'V': {'free': 0.5, 'workers': 0.4}}

words = ['free', 'workers']
v = {}
path = {}

for s in states:
    v[s] = start[s] * emit[s][words[0]]
    path[s] = [s]

for word in words[1:]:
    nv, np = {}, {}
    for s in states:
        prob, prev = max((v[p]*trans[p][s], p) for p in states)
        nv[s] = prob * emit[s][word]
        np[s] = path[prev] + [s]
    v, path = nv, np

best = max(v, key=v.get)
print("Best POS Tags:", path[best])