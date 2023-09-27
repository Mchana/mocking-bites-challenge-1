from lib.task import Task

class TaskFormatter:
    def __init__(self, task): # task is an instance of Task
        self.task = task

    def format(self):
        if self.task.complete == True:
            return f"- [x] {self.task.title}"
        else:
            if self.task.complete == False:
                return f"- [ ] {self.task.title}"
        # Returns the task formatted as a string.
        # If the task is not complete, the format is:
        # - [ ] Task title
        # If the task is complete, the format is:
        # - [x] Task title
        pass