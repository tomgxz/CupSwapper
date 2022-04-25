def swapper(paths):
    a,b,c=0,1,0; compare=["a","b","c"]
    for swap in paths:
        move=list(swap.lower())
        pos1=compare.index(move[0])
        pos2=compare.index(move[1])
        if 0 not in [pos1,pos2]: a,b,c=a,c,b
        elif 1 not in [pos1,pos2]: a,b,c=c,b,a
        elif 2 not in [pos1,pos2]: a,b,c=b,a,c
    return compare[[a,b,c].index(1)].upper()

input(swapper(["AB"]))
