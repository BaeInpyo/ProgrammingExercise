"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3394/

This problem is topologicall sort.
In tpsort, we do
    - detect cycle if exist
    - sort topologically
We have 2 solutions for tpsort, BFS and DFS.
In both solutions, checking existence of cycle is easy.
In BFS, if queue is empty before popping N elements, it means cycle.
In DFS, if result of tpsort does not contain all N nodes, it means cycle.
"""

from collections import deque
import sys

sys.setrecursionlimit(10000)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = dict()
        indegree = [0] * numCourses

        # Build graph
        for (node1, node2) in prerequisites:
            if node2 in graph:
                graph[node2].append(node1)
            else:
                graph[node2] = [node1]

            indegree[node1] += 1

        # return self.BFS(numCourses, graph, indegree)
        return self.DFS(numCourses, graph, indegree)
        
    def BFS(self, numCourses, graph, indegree):
        # Start BFS from root of each trees
        queue = deque()

        # BFS from root node which does not have indegree
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)

        answer = []
        for _ in range(numCourses):
            # cycle exists
            if not queue:
                return []

            src = queue.popleft()
            answer.append(src)
            for dst in graph.get(src, []):
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    queue.append(dst)

        return answer

    def DFS(self, numCourses, graph, indegree):
        """DFS solution"""
        tpsort = []

        # We need to boolean list to check cycle
        # visited[i] means node i is visited
        # finished[i] means node i is added to result of tpsort
        visited = [False] * numCourses
        finished = [False] * numCourses
        for node in range(numCourses):
            if indegree[node] == 0:
                self._DFS(graph, visited, finished, node, tpsort)

        # This means cycle exists
        if len(tpsort) < numCourses:
            return []

        # reverse order of DFS is result of tpsort
        return tpsort[::-1]

    def _DFS(self, graph, visited, finished, src, tpsort):
        """Body of DFS"""
        visited[src] = True

        for dst in graph.get(src, []):
            # cycle exists
            if visited[dst] and not finished[dst]:
                print("dst is already visited but not finished:", dst)
                return

            if not visited[dst]:
                self._DFS(graph, visited, finished, dst, tpsort)

        # Mark as visited and add to tpsort list
        finished[src] = True
        tpsort.append(src)

        return
