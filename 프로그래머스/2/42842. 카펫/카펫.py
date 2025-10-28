def solution(brown, yellow):
    answer = []
    total_tiles = brown + yellow 
    for height in range(3, total_tiles + 1):
        if total_tiles % height == 0:
            width = total_tiles // height

            if width < height:
                continue
            if (width - 2) * (height - 2) == yellow:
                answer = [width, height]
                break
    return answer