# Task Scheduling Problem (Optimization).
'''
A software engineer has multiple tasks to complete. Each task has:
• a deadline (day by which it must be finished),
• an amount of time it takes to complete (in days).
Write a Python function to:
• Determine the maximum number of tasks the engineer can complete without missing
deadlines.
Input Example:
tasks = [
{'name': 'Task 1', 'deadline': 4, 'duration': 2},
{'name': 'Task 2', 'deadline': 3, 'duration': 1},
{'name': 'Task 3', 'deadline': 2, 'duration': 1},
{'name': 'Task 4', 'deadline': 1, 'duration': 2},
]
'''

def task_scheduling(tasks):
    tasks.sort(key=lambda x: (x['deadline'], x['duration']))
    completed_tasks = []
    time = 0
    for task in tasks:
        if time + task['duration'] <= task['deadline']:
            completed_tasks.append(task)
            time += task['duration']
    return completed_tasks

tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]
print(task_scheduling(tasks))
