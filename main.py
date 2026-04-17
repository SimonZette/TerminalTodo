import display
import model


def main():
    c = model.Context("My stuff")
    print(c.cursor.col, c.cursor.row)
    
    c.board.add_task("task 1")
    c.board.add_task("task 2")
    c.move_cursor_to(model.State.UPCOMING, 1)
    
    c.move_cursor_to(model.State.UPCOMING, 999)

    c.move_cursor_up()

    c.move_cursor_down()

    c.board.add_task("this is a long long long task", model.State.PAUSED)
    c.board.add_task("task 4", model.State.DONE)
    c.move_cursor_right()
    print(c.cursor.col, c.cursor.row)

    display.display_context(c)


if __name__ == "__main__":
    main()
