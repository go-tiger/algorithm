def solution(id_pw, db):
    answer = 'fail'
    for user_info in db:
        if id_pw[0] == user_info[0]:
            if id_pw[1] == user_info[1]:
                answer = 'login'
            else:
                answer = 'wrong pw'
            break
    return answer