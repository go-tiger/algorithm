def solution(rank, attendance):
    ranked_students_info = []
    for i in range(len(rank)):
        ranked_students_info.append((rank[i], i, attendance[i]))

    ranked_students_info.sort()

    selected_students_original_indices = []
    for r, original_idx, attended in ranked_students_info:
        if attended:
            selected_students_original_indices.append(original_idx)
        if len(selected_students_original_indices) == 3:
            break

    return (10000 * selected_students_original_indices[0]) + \
           (100 * selected_students_original_indices[1]) + \
           (selected_students_original_indices[2])