class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {}
        taken = [True for _ in range(numCourses)]
        visited = [True for _ in range(numCourses)]
        stack = []
        for e in prerequisites:
            if e[0] in prereq:
                prereq[e[0]].append(e[1])
            else:
                prereq[e[0]] = [e[1]]
                taken[e[0]] = False
                visited[e[0]] = False
                stack.append(e[0])
        
        if not stack:
            return [i for i in range(numCourses)]
        
        result = []
        for i in range(numCourses):
            if taken[i]:
                result.append(i);
        
        while stack:
            if len(stack) > 2*numCourses:
                return []
            c = stack[-1]
            if not visited[c]:
                can_take = True
                for p_c in prereq[c]:
                    if not taken[p_c]:
                        can_take = False
                        stack.append(p_c)
                if can_take:
                    visited[c] = True
                    taken[c] = True
                    result.append(c)
                    stack.pop()
            else:
                if not taken[c]:
                    return []
                else:
                    stack.pop()
            
        return result
