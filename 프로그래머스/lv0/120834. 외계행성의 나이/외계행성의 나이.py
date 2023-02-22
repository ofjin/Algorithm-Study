def solution(age):
    answer = ''
    eng_age = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    
    for i in str(age):
        answer += eng_age[int(i)]
        
    return answer