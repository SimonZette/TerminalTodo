import model

def display_context(c: model.Context):
    # Headers
    print(c.project_name)
    print("#########################################################################")
    print("UPCOMING         # ONGOING          # PAUSED           # DONE")
    print("                 #                  #                  #")

    # Tasks
    highest_row = 0
    for state in model.State:
        highest_row = max(highest_row, len(c.board[state]))
        
    for row in range(0, highest_row+1):
        for state in model.State:
            if len(c.board[state]) > row:
                if c.cursor == model.Cursor(state, row):
                    print(">", end="")
                else:
                    print("-", end="")
                    
                task = c.board[state][row]
                if len(task) > 15:
                    print(task[:12], "...", sep="", end="")
                else:
                    print(task, " "*(15-len(task)), sep="", end="")

            else:
                print("                ", end="")
                
            if state != model.State.DONE:
                print(" # ", end="")
                
        print()
                
