

name = "Dave"


def another():
    color = "blue"
    print(color)
    print(name)

    def greeting(name):
        print(color)
        print(name)

    greeting("Dave")


another()
