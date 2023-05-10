def solution(s):
    list = s.split(' ')
    answer = 0

    for i in range (0, len(list)):
        if (list[i] == 'Z'):
            answer -= int(list[i-1])
        else:
            answer += int(list[i])
            
    return answer