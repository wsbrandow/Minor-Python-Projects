def median(x):
    xsort = sorted(x)
    if len(xsort) % 2 == 0:
        right = len(xsort) / 2
        left =(len(xsort) / 2) - 1
        return (xsort[right] + xsort[left]) / 2.0
    else:
        return xsort[len(xsort) / 2]
