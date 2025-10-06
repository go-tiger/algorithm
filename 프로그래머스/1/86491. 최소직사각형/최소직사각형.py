def solution(sizes):
    max_dims = []
    min_dims = []

    for width, height in sizes:
        max_dims.append(max(width, height))
        min_dims.append(min(width, height))
    return max(max_dims) * max(min_dims)