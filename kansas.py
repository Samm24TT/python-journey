from random import choice

capital = "Topeka"

bird = "Western Medowlark"

flower = "Sumflower"

song = "Home on the Range"


def randomfunfact():
    funfacts = [
        "Kansa is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansas are annoyed by Wizard of Oz refrences from people outside of kansa."
    ]

    index = choice("0123")

    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfunfact()
