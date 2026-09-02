class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.seen = set()
        self.graph = defaultdict(list)
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

        def dfs(node, parent):
            if node in self.seen:
                return False
            self.seen.add(node)
            for child in self.graph[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            return True
        
        
        res = dfs(0, -1)
        if len(self.seen) == n:
            return res
        return False

