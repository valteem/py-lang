def round_grades(grades):
    rounded = []
    for x in grades:
        if x < 38:
            y = x
        else:
            cap = (int(x/5) + 1)*5 
            if (cap - x) < 3:
                y = cap
            else:
                y = x
        rounded.append(y)
    return rounded