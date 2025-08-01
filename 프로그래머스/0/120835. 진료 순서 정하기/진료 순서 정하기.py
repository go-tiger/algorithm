def solution(emergency):
    sort_emergency = sorted(emergency, reverse=True)
    return [sort_emergency.index(v) + 1 for v in emergency]