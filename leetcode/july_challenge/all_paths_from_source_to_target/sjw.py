"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3400/

Do DFS search from src and check if curr node is dst node
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        visited = [False] * n
        return self.dfs(graph, visited, 0, n-1)

    def dfs(self, graph, visited, src, dst):
        """Do DFS from src node and return path"""
        if src == dst:
            return [[src]]

        answer = []
        for next_ in graph[src]:
            visited[next_] = True
            result = self.dfs(graph, visited, next_, dst)
            if result:
                answer.extend([[src] + path for path in result])

        return answer