from enum import Enum


class State(Enum):
    UPCOMING = 0
    ONGOING = 1
    PAUSED = 2
    DONE = 3

class Board:
    lists = {}

    def __init__(self):
        for state in State:
            self.lists[state] = []

    def __getitem__(self, state: State) -> list[str]:
        return self.lists[state]

    def has_task(self, task: str) -> bool:
        for state in State:
            if task in self.lists[state]:
                return True
        return False

    def add_task(self, task: str, task_state: State = State.UPCOMING):
        if self.has_task(task):
            raise ValueError("cannot add a task that the todo-board already has")
        self.lists[task_state].append(task)
        
    def remove_task(self, task: str):
        if not self.has_task(task):
            raise ValueError("cannot remove a task that the todo-board does not have")
        for state in State:
            if task in self.lists[state]:
                self.lists[state].remove(task)

    def move_task(self, task: str, task_state: State):
        if not self.has_task(task):
            raise ValueError("cannot move a task that the todo-board does not have")
        self.remove_task(task)
        self.add_task(task, task_state)
