def solution(num_list):
    last = num_list[-1]
    last2 = num_list[-2]

    if last > last2:
        num_list.append(last - last2)
    else:
        num_list.append(last * 2)

    return num_list