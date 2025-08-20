from queue import Queue

task_queue = Queue()

def add_to_queue(task):
    task_queue.put(task)

def get_next_task():
    if not task_queue.empty():
        return task_queue.get()
    return None
