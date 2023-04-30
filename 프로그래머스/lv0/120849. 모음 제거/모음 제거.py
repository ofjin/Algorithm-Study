def solution(my_string):
    answer = ''
    search = 'aeiou'
    
    for char in my_string:
        if char not in search:
            answer += char
    return answer