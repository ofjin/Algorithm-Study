def solution(array):
    array.sort()
    center_index = len(array) // 2
    answer = array[center_index]
    return answer