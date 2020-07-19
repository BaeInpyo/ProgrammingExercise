"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3394/

This problem is related to topological sort at my first glance.
To sort topologically, I can use dfs. When we start dfs from nodes wihtout
inbound edges, we can get reversed order of tp sort.

Additionally, we must detect cycle 
"""

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # use queue and bfs
        graph = dict()
        indegree = [0] * numCourses

        for (node1, node2) in prerequisites:
            if node2 in graph:
                graph[node2].append(node1)
            else:
                graph[node2] = [node1]

            indegree[node1] += 1

        queue = deque()
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

    #     # edge(u, v) means we must observe u -> v order
    #     graph = dict()  # key: prerequisite, value: list of subjects
    #     existIngress = [False] * numCourses
    #     for (subject, prerequisite) in prerequisites:
    #         # build graph
    #         if prerequisite in graph:
    #             graph[prerequisite].append(subject)
    #         else:
    #             graph[prerequisite] = [subject]

    #         existIngress[subject] = True

    #     # do dfs only for nodes without ingress
    #     visited = [False] * numCourses
    #     tpsort = []
    #     for src in range(numCourses):
    #         if existIngress[src]:
    #             continue
    #         is_cycle = self.dfs(graph, src, visited, tpsort)
    #         if is_cycle:
    #             print("cycle exists")
    #             return []

    #     print("no cycle")
    #     # cycle does not exist
    #     return tpsort[::-1]

    # def dfs(self, graph, src, visited, tpsort):
    #     """Do DFS from src node and add node to tpsort
    #     Return False if cycle exists
    #     """

    #     if visited[src]:
    #         return True

    #     for dst in graph.get(src, []):
    #         print("dfs:", src, "->", graph.get(src, []), "curr dst:", dst)
    #         # cycle detected
    #         if visited[dst]:
    #             return False

    #         if not visited[dst]:
    #             self.dfs(graph, dst, visited, tpsort)

    #     print("visit:", src)
    #     visited[src] = True
    #     tpsort.append(src)

    #     return False