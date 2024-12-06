'''
This Python code processes a 2D grid and simulates the movement of a guard.
Credit: https://reddit.com/user/4HbQ/
This is my first time seeing complex numbers being used in code and have gained valuable knowledge by studying this script.
'''

G = {i+j*1j: c for i,r in enumerate(open('day-6/puzzle_input.txt'))
               for j,c in enumerate(r.strip())}

start = min(p for p in G if G[p] == '^')

def walk(G):
    pos, dir, seen = start, -1, set()
    while pos in G and (pos,dir) not in seen:
        seen |= {(pos,dir)}
        if G.get(pos+dir) == "#":
            dir *= -1j
        else: pos += dir
    return {p for p,_ in seen}, (pos,dir) in seen

path = walk(G)[0]
print(len(path),
      sum(walk(G | {o: '#'})[1] for o in path))