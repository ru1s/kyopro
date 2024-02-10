def FloydWarshall(G : list, INF = 10**18):

    n = len(G)
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        for v in G[i]:
            u, w = v
            dist[i][u] = w
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] == INF or dist[k][j] == INF:
                    continue
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist