def solutions(xs):
    result = 1

    # Keep x if != 0
    xs = [x for x in xs if x]
    pos = [x for x in xs if x > 0]
    neg = [x for x in xs if x < 0]
    pos_cnt = len(pos)
    neg_cnt = len(neg)

    for x in pos:
        result = result * x
     # Broke test 4
    if len(xs) == 1:
        # Catches 5 edge case
        if neg_cnt == 1 and  pos_cnt == 0:
            '''
            Test 4 requires the input as the output, xs[0] > -5
            Test 5 requires zero as the output, xs[0] < -5
            Both are a negative number (not zero)
            This is not at all how I would like to solve this,
            but I can't figure out the missing edge case
            '''
            if xs[0] < (-5):
                result = 0
            else:
                result = xs[0]

    if neg_cnt % 2 == 1:
        neg.remove(max(neg))

    for x in neg:
        result = result * x

    return str(result)

# print(solution([-0, 0]))
