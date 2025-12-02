def solution(k, dungeons):
    max_dungeons_count = 0
    num_dungeons = len(dungeons)
    visited = [False] * num_dungeons

    def dfs(current_count, remaining_k):
        nonlocal max_dungeons_count
        max_dungeons_count = max(max_dungeons_count, current_count)

        for i in range(num_dungeons):
            required_fatigue, consumed_fatigue = dungeons[i][0], dungeons[i][1]

            if not visited[i] and remaining_k >= required_fatigue:
                visited[i] = True
                dfs(current_count + 1, remaining_k - consumed_fatigue)
                visited[i] = False

    dfs(0, k)
    return max_dungeons_count