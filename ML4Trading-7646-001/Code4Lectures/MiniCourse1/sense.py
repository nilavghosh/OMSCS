
p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q = []
    for i,w in enumerate(world):
        if(w == Z):
            q.append(p[i] * pHit)
        else:
            q.append(p[i] * pMiss)
    return ([n/sum(q) for n in q]) 

if __name__ == "__main__":
    print (sense(p,Z))
