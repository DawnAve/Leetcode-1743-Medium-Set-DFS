class Solution:
    def restoreArray(self, adj: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u,v in adj:
            graph[u].append(v)
            graph[v].append(u)
        first = None
        for i in graph:
            if len(graph[i]) == 1:
                first = i
                break

        ret = []
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            ret.append(node)
            for connect in graph[node]:
                dfs(connect)

        dfs(first)
        return ret
                
