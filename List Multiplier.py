def product(x):
    new_number = 1
    for number in x:
        if number != 0:
            new_number *= number
        elif number == 0:
            new_number = 0
    return new_number
