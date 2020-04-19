factorials = [1]
for num in range(1, 15):
    factorials.append(factorials[-1] * num)
def nCr(n, r):
    return factorials[n] // factorials[r] // factorials[n-r]
def solution(n):
    def dfs(visited_set, visited_list, curr_pos, remain):
        """
        visited: set of visited positions
        curr_pos: current position
        remain: remain sum
        """

        if len(visited_set) >= 500:
            return False

        r, k = curr_pos
        curr_value = nCr(r-1, k-1)
        if curr_value > remain:
            return False

        visited_set.add(curr_pos)
        visited_list.append(curr_pos)
        # print("add: ", curr_pos, "value:", curr_value, "remain:", remain)
        remain -= curr_value
        if remain == 0:
            return True

        adjacent = [
            (r-1, k-1),
            (r-1, k),
            (r, k-1),
            (r, k+1),
            (r+1, k),
            (r+1, k+1)
        ]
        adjacent = [pos for pos in adjacent if pos[0] >= 1 and pos[1] >= 1 and pos[0] >= pos[1]]
        adjacent = [pos for pos in adjacent if pos not in visited_set]
        adjacent.sort(key=lambda x: -nCr(x[0]-1, x[1]-1))   # sort by nCr DESC

        for pos in adjacent:
            result = dfs(visited_set, visited_list, pos, remain)
            if result:
                return True

        # there is no result
        visited_set.remove(curr_pos)
        visited_list.pop()
        return False


    visited_set = set()
    visited_list = list()
    result = dfs(visited_set, visited_list, (1, 1), n)
    for pos in visited_list:
        r, k = pos
        print(r, k)
        # print(r, k, nCr(r-1, k-1))



if __name__ == "__main__":
    T = int(input())
    for case_num in range(1, T+1):
        N = int(input())
        print("Case #{}: ".format(case_num))
        solution(N)