def solution(emergency):
    answer = []
    tmp = sorted(emergency, reverse = True)
    
    answer = [tmp.index(i)+1 for i in emergency]
    return answer