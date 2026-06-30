class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph=defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
        dist=[9999]*n
        dist[src]=0
        pq=[(0,src)]
        while pq:
            d,u=heapq.heappop(pq)
            if d>dist[u]:
                continue
            for v,w in graph[u]:
                if d+w<dist[v]:
                    dist[v]=d+w
                    heapq.heappush(pq,(d+w,v))
        for i in range(len(dist)):
            if dist[i]==9999:
                dist[i]=-1
        return {node: d for node, d in enumerate(dist)}

