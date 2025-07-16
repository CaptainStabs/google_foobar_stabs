def solution(x, y):

    if len(x) > len(y):
        solution_list = [integer for integer in x if integer not in y]
    else:
        solution_list = [integer for integer in y if integer not in x]
    return solution_list[0]
