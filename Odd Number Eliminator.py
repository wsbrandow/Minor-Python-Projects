def purify(xlist):
    evens = []
    for integer in xlist:
        if integer % 2 == 0:
            evens.append(integer)
    return evens
