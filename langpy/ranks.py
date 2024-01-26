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

def convert_str_to_list_of_int(s: str) -> list[int]:
    """
    https://stackoverflow.com/a/8270124
    To remove all whitespace characters (space, tab, newline, and so on) you can use split() then join()
    """
    if ''.join(s.split()).isdigit():
        return list(map(int, s.rstrip().split()))
    else:
        return []