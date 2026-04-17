import model


def main():
    b = model.Board()
    
    b.add_task("Say 'Hello, World!'")
    print(b[model.State.UPCOMING], b[model.State.ONGOING])

    b.move_task("Say 'Hello, World!'", model.State.ONGOING)
    print(b[model.State.UPCOMING], b[model.State.ONGOING])
    
    b.remove_task("Say 'Hello, World!'")
    print(b[model.State.UPCOMING], b[model.State.ONGOING])


if __name__ == "__main__":
    main()
