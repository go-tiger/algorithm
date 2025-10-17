import heapq

def solution(k, score):
    answer = []
    honor_k_heap = []
    for s in score:
        if len(honor_k_heap) < k:
            heapq.heappush(honor_k_heap, s)
        else:
            if s > honor_k_heap[0]:
                heapq.heapreplace(honor_k_heap, s)
        answer.append(honor_k_heap[0])
    return answer