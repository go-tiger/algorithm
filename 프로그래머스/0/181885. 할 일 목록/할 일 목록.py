def solution(todo_list, finished):
    return [task for task, done in zip(todo_list, finished) if not done]