def solution(record):
    temp = []
    answer = []

    for r in record:
        command = r.split()[0]
        if command == 'RECEIVE':
            address = r.split()[1]
            temp.append(address)
        elif command == 'DELETE':
            if temp:
                temp.pop(-1)
        elif command == 'SAVE':
            if temp:
                answer.extend(temp)
                temp = []

    return answer