import model


def main():
    c = model.Context()
    print(c.cursor.col, c.cursor.row)
    
    c.board.add_task("task 1")
    c.board.add_task("task 2")
    c.move_cursor_to(model.State.UPCOMING, 1)
    print(c.cursor.col, c.cursor.row)
    
    c.move_cursor_to(model.State.UPCOMING, 999)
    print(c.cursor.col, c.cursor.row)

    c.move_cursor_up()
    print(c.cursor.col, c.cursor.row)

    c.move_cursor_down()
    print(c.cursor.col, c.cursor.row)

    c.board.add_task("task 3", model.State.PAUSED)
    c.board.add_task("task 4", model.State.DONE)
    c.move_cursor_right()
    print(c.cursor.col, c.cursor.row)


if __name__ == "__main__":
    main()
