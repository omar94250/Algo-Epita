from GraphMat import GraphMat
from Graph import Graph
from AlgoPy import queue
from AlgoPy.queue import Queue
import graphviz as gv

def addEdge(G, src, dst):
    if src < 0 or src >= G.order:
        raise Exception("Invalid src")
    if dst < 0 or dst >= G.order:
        raise Exception("Invalid dst")
    G.adj[src][dst] += 1
    if not G.directed and src != dst:
        G.adj[dst][src] += 1
    return G

def addEdgeAdj(G, src, dst):
    if src < 0 or src >= G.order:
        raise Exception("Invalid src")
    if dst < 0 or dst >= G.order:
        raise Exception("Invalid dst")
    G.adjLists[src].append(dst)
    if not G.directed and src != dst:
        G.adj[dst].append(src)

def toDot(G):
    file = open("graphMat.dot", 'w')
    if G == None:
        return ' '
    if G.directed:
        s = "digraph G{\n"
        sep = " -> "
    else:
        s = "graph G{\n"
        sep = " -- "
    for i in range (G.order):
        jMax = G.order if G.directed else i + 1
        for j in range (jMax):
            for k in range(G.adj[i][j]):
                s += ' ' + str(i) + sep + str(j) + '\n'
    s += "}\n"
    file.write(s)
    file.close
    return s

def toDotAdj(G):
    if G == None:
        return ' '
    if G.directed:
        s = "digraph G{\n"
        sep = " -> "
    else:
        s = "graph G{\n"
        sep = " -- "
    for i in range (G.order):
        jMax = G.order if G.directed else i + 1
        for j in range (G.adjLists[i]):
            if j < jMax:
                s += ' ' + str(i) + sep + str(j) + '\n'
    s += "}\n"
    return s

def fromGRAMat(filename):
    file = open(filename, 'r')
    directed = (0 != int(file.readline().strip()))
    order = int(file.readline().strip())
    G = GraphMat(oder, directed)
    for line in file.readline:
        line = line.strip().split()
        addEdge(G, int(line[0]), int(line[1]))
    file.close()
    return G

def fromGRA(filename):
    file = open(filename, 'r')
    directed = (0 != int(file.readline().strip()))
    order = int(file.readline().strip())
    G = Graph(oder, directed)
    for line in file.readline:
        line = line.strip().split()
        addEdge(G, int(line[0]), int(line[1]))
    file.close()
    return G

def __bfs(G, src, M):
    Q = Queue()
    Q = queue.enqueue(src, Q)
    M[src] = -1
    while not queue.isEmpty(Q):
        src = queue.dequeue(Q)
        for dst in range (G.order):
            if G.adj[src][dst] > 0 and M[dst] == None:
                Q = queue.enqueue(dst, Q)
                M[dst] = src

def bfs(G, src):
    M = [ None ] * G.order
    __bfs(G, src,  M)
    for som in range(G.order):
        if M[som] == None:
            __bfs(G, som, M)
    return M

def __bfsAdj(G, src, M):
    Q = Queue()
    Q = queue.enqueue(G, Q)
    M[src] = -1
    while not queue.isEmpty(Q):
        src = queue.dequeue(Q)
        for dst in G.adjLists[src]:
            if M[dst] == None:
                Q = queue.enqueue(dst, Q)
                M[dst] = src

def bfsAdj(G, src):
    M = [ None ] * G.order
    __bfsAdj(G, src,  M)
    for som in range(G.order):
        if M[som] == None:
            __bfsAdj(G, som, M)
    return M

def __dfsMat(G, src, M):
    for dst in range(G.order):
        if G.adj[src][dst] > 0:
            if M[dst] == None:
                M[dst] = src
                print('edge', src, '->', dst)
                __dfsMat(G, dst, M)
            elif M[src] != dst:
                print('back edge', src, '->', dst)

def dfsMat(G, src):
    M = [ None ] * G.order
    M[src] = -1
    __dfsMat(G, src, M)
    for som in range(G.order):
        if M[som] == None:
            M[som] = - 1
            __dfsMat(G, som, M)
    return M

def __dfsAdj(G, src, M, cpt, preff, suff):
    cpt += 1
    pref[src] = cpt
    # Successors
    for dst in ajdLists[src]:
        if M[dst] == None:
            M[dst] = src
            print('edge', src, '->', dst)
            cpt = __dfsAdj(G, dst, M, cpt, preff, suff)
        elif pref[src] < pref[dst]:
            print('forward edge', src, '->', dst)
        elif suff[dst] == None:
            print('back edge', src, '->', dst)
        else:
            print('cross edge', src, '->', dst)
    # Suffix
    cpt += 1
    suff[src] = cpt
    return cpt

def dfsAdj(G, src):
    M = [ None ] * G.order
    preff = [ None ] * G.order
    suff = [ None ] * G.order
    cpt = 0
    M[src] = -1
    cpt = __dfsAdj(G, src, M, cpt, preff, suff)
    for som in range(G.order):
        if M[som] == None:
            M[som] = - 1
            cpt = __dfsAdj(G, som, M, cpt, preff, suff)
    return M
