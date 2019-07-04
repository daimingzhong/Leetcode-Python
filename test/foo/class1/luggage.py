def luggage(weights):
    answer = ""

    # Insert you code here

    return answer


res = luggage("1,2,3,4,5,6,7")
print(res)


def luggage(weights):
    ls = weights.split(',')
    que = []
    local = []
    for ss in ls:
        local.append(ss)
        if len(local) == 3:
            que.append(local)
            local = []
    len(local) > 0 and que.append(local)
    return ','.join([','.join(local) for local in que[::-1]])