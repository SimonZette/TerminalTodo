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

    def __bool__(self) -> bool:
        for state in State:
            if self.lists[state]: # Is not empty
                return True
        return False

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

class Cursor:
    col: State
    row: int

    def __init__(self, col: State = State.UPCOMING, row: int = 0):
        self.col = col
        self.row = row

    def __eq__(self, other) -> bool:
        return self.col == other.col and self.row == other.row

class Context:
    board = Board()
    cursor = Cursor()
    project_name: str

    def __init__(self, project_name: str):
        self.project_name = project_name

    def clamp_row(self):
        self.cursor.row = min(self.cursor.row, len(self.board[self.cursor.col]) - 1)

    def move_cursor_to(self, col: State, row: int):
        if not self.board: # Is empty
            raise ValueError("cannot move on an empty todo-board")
        if row < 0:
            raise ValueError("cannot move to a row less than 0")
        if not self.board[col]: # Is empty
            raise ValueError("cannot move to an empty column")

        self.cursor = Cursor(col, row)
        self.clamp_row()

    def move_cursor_up(self):
        if not self.board: # Is empty
            raise ValueError("cannot move on an empty todo-board")
        if self.cursor.row == 0:
            raise ValueError("cannot move to a row less than 0")

        self.cursor.row -= 1

    def move_cursor_down(self):
        if not self.board: # Is empty
            raise ValueError("cannot move on an empty todo-board")
        if self.cursor.row == len(self.board[self.cursor.col]) - 1:
            raise ValueError("cannot move to a row higher than the highest row in its column")

        self.cursor.row += 1

    def move_cursor_left(self):
        if not self.board: # Is empty
            raise ValueError("cannot move on an empty todo-board")
        if self.cursor.col == State.UPCOMING:
            raise ValueError("cannot move to the left of the left-most column")
        
        for i in reversed(range(State.UPCOMING.value, self.cursor.col.value)):
            if len(self.board[State(i)])-1 >= self.cursor.row:
                self.cursor.col = State(i)
                return
            
        for i in reversed(range(State.UPCOMING.value, self.cursor.col.value)):
            if self.board[State(i)]:
                self.cursor.col = State(i)
                self.clamp_row()
                return

        raise ValueError("cannot move to the left as there are no tasks to the left")

    def move_cursor_right(self):
        if not self.board: # Is empty
            raise ValueError("cannot move on an empty todo-board")
        if self.cursor.col == State.DONE:
            raise ValueError("cannot move to the right of the right-most column")

        for i in range(self.cursor.col.value+1, State.DONE.value+1):
            if len(self.board[State(i)])-1 >= self.cursor.row:
                self.cursor.col = State(i)
                return
            
        for i in range(self.cursor.col.value+1, State.DONE.value+1):
            if self.board[State(i)]:
                self.cursor.col = State(i)
                self.clamp_row()
                return

        raise ValueError("cannot move to the right as there are no tasks to the right")
