def validate_integer(size: str, least_value: int = None, largest_value: int = None):
    """
    Function validating size or index
    :param size: entry that supposed inform list size or index
    :param least_value: value that is the acceptable minimum
    :param largest_value: value that is the acceptable maximum
    :return: valid integer size or Exception if impossible
    """

    valid_size = int(size)
    if least_value is not None and valid_size < least_value:
        raise ValueError

    if largest_value is not None and valid_size > largest_value:
        raise ValueError

    return valid_size


def validate_float(entry: str):
    """
    Function validating float
    :param entry: entry that supposed to be float
    :return: valid integer size or Exception if impossible
    """

    valid_value = float(entry)
    # asserting NaN
    if valid_value != valid_value:
        raise TypeError

    return valid_value


def validate_range(lesser, greater, *args):
    """
    Validates rang
    :param lesser: string, supposed to be lower bound
    :param greater: string, supposed to be upper bound
    :return: tuple that is range of values
    """
    a = float(lesser)
    b = float(greater)

    # too many arguments, raise an Error
    if args:
        raise TypeError

    # sifting nan's
    if a != a or b != b:
        raise TypeError
    # sifting invalid range order
    elif a > b:
        raise ValueError

    else:
        return a, b


def validate_iterable_values(iterable, type_cast):
    """
    Function validating iterable
    :param iterable: iterable to validate (has .append method!)
    :param type_cast: type for elements to be casted
    :return: validated iterable
    """

    cls = type(iterable)
    result = cls.__new__(cls)
    result.__init__()

    for element in iterable:
        try:
            casted_element = type_cast(element)
        except ValueError:
            continue
        else:
            result.append(casted_element)

    return result


def validate_iterable_size(iterable, size: int):
    """
    Function validating size of iterable with supposed
    If there are too much values inside, they will be erased (from head)
    If there are not enough elements, it raises AssertionError
    :param iterable: iterable to check (with len() and .pop() support)
    :param size: supposed size of iterable
    :return: changes iterable to valid form
    """

    if len(iterable) < size:
        raise AssertionError

    while len(iterable) > size:
        iterable.pop()

    return
