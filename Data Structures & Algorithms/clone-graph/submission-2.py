"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        self.copy = Node()
        self.seen_edges = set()
        self.seen_verts = {}

        def dfs(old, new):
            if old:
                print(old.val)
                new.val = old.val
                print(new.val)
                self.seen_verts[old] = new
                for neighbor in old.neighbors:
                    if neighbor and (old, neighbor) not in self.seen_edges:
                        self.seen_edges.add((old, neighbor))
                        if self.seen_verts.get(neighbor, None) is not None:
                            new.neighbors.append(self.seen_verts[neighbor])
                        else:
                            new.neighbors.append(Node())
                            dfs(neighbor, new.neighbors[-1])
        dfs(node, self.copy)
        return self.copy
