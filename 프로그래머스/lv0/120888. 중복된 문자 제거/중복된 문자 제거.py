def solution(my_string):
    my_list = list(my_string)
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)

    return ''.join(i for i in new_list)