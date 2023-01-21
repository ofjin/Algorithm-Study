import statistics

def solution(array):
    num_arr = statistics.multimode(array)
    
    if (len(num_arr) == 1):
        return num_arr[0]
    else:
        return -1