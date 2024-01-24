def ginortS(string):
    """
    Sort an Input String with the following rules:
    1. Lowercase letter come first, sorted alphabetically 
    2. Uppercase letters come next, sorted alphabetically
    3. Odd digits come next, sorted ascending
    4. Even digits come next, sorted ascending

    Args:
        string (str): Input String
    """
    lower = sorted([x for x in string if x.islower()])
    upper = sorted([x for x in string if x.isupper()])
    number = sorted([int(x) for x in string if x.isdigit()], key=lambda x:(-(x % 2), x))
    number = [str(x) for x in number]
    arr = lower + upper + number
    return "".join(arr)
    

