def dead_ants_count(ant):
    if not ant:                          
        return 0
    ants_dead = ant.replace("ant", "")
    head = ants_dead.count("a")
    body = ants_dead.count("n")
    tail = ants_dead.count("t")
    return max (head, body, tail)

problem = "...ant...ant..na..t.ant.t..ant...ant..ant..ant.anant..t"
dead_ants = dead_ants_count(problem)
print("Dead ants:", dead_ants)