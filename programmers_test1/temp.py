def solution(a):
    if len(a) <= 3:
        return len(a)
    
    n = len(a)
    left_min = [0] * n
    left_min[0] = a[0]
    right_min = [0] * n
    right_min[n-1] = a[n-1]
    
    for idx in range(1, n):
        left_min[idx] = min(left_min[idx-1], a[idx])
    for idx in reversed(range(n-1)):
        right_min[idx] = min(right_min[idx+1], a[idx])
        
    answer = 2  # 좌우 끝은 무조건 됨
    for idx in range(1, n-1):
        if left_min[idx-1] > a[idx] or right_min[idx+1] > a[idx]:
            answer += 1
            
    print("answer:", answer)
    print("array is : {}".format(a))
    print("left_min: {}".format(left_min))
    print("right_min: {}".format(right_min))

solution([9,-1,-5])
solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])
