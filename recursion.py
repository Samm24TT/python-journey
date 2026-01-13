

def add_num(num):

    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_num(total)


mynewtotal = add_num(0)
print(mynewtotal)
