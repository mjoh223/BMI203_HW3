num_rab = []
def rabbits(n):
    if n <= 1:
        return 1
    return (rabbits(n-1)+rabbits(n-2))
    rab = rabbits(n-1)+rabbits(n-2)
    num_rab.append(rab)
    return (num_rab[n-1] + num_rab[n-2])

rabbits(10)

def rabbits_bu(n):
    counts = [1,1]
    for i in range(2, n):
        counts.append(counts[i -1] + counts[i -2])
    return counts[i]
rabbits_bu(10)
