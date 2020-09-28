import string

def solution(new_id):
    answer = new_id
    
    # step 1: uppercase to lowercase
    answer = answer.lower()
    
    # step 2: remove invalid characters
    valid_characters = string.ascii_lowercase + string.digits + "-" + "_" + "."
    answer = "".join([char for char in answer if char in valid_characters])
    
    # step 3: replace multiple "."s to "."
    while ".." in answer:
        answer = answer.replace("..", ".")
        
    # step 4: removing leading/trailing "."
    if answer and answer[0] == ".":
        answer = answer[1:]
    if answer and answer[-1] == ".":
        answer = answer[:-1]
        
    # step 5: if answer is empty, assign "a"
    if not answer:
        answer = "a"
        
    # step 6
    answer = answer[:15]
    if answer[-1] == ".":
        answer = answer[:-1]
        
    # step 7
    if len(answer) <= 2:
        while len(answer) < 3:
            answer = answer + answer[-1]
            
    print("answer:", answer)
    return answer
    

solution("...!@BaT#*..y.abcdefghijklm")
