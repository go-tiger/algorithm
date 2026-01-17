def solution(N, stages):
    answer_list = []
    stage_counts = [0] * (N + 2)
    
    for stage in stages:
        stage_counts[stage] += 1
        
    total_players_reached_or_passing = len(stages)
    
    for i in range(1, N + 1):
        players_at_current_stage = stage_counts[i]
        
        if total_players_reached_or_passing == 0:
            fail_rate = 0
        else:
            fail_rate = players_at_current_stage / total_players_reached_or_passing
        
        answer_list.append((i, fail_rate))
        total_players_reached_or_passing -= players_at_current_stage
        
    answer_list.sort(key=lambda x: (-x[1], x[0]))
    
    return [stage_number for stage_number, _ in answer_list]
