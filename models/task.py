class Task:
    def __init__(self, item):
        self.item = item
        self.taskId = item["TaskId"]
        self.name = item["TaskName"]
