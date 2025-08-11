def solution(arr):
    prev_arr_state = list(arr) 
    count = 0
    while True:
        current_arr_state = []
        changed = False
        for num in prev_arr_state:
            if num >= 50 and num % 2 == 0:
                new_num = num // 2
            elif num < 50 and num % 2 != 0:
                new_num = num * 2 + 1
            else:
                new_num = num
            current_arr_state.append(new_num)
            if new_num != num:
                changed = True
        if not changed:
            break
        prev_arr_state = current_arr_state
        count += 1
    return count