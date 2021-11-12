import os


def validate_value(type_cast, size: str, least_value: int = None, largest_value: int = None):
    """
    Function validating size or index
    :param type_cast:
    :param size: entry that supposed inform list size or index
    :param least_value: value that is the acceptable minimum
    :param largest_value: value that is the acceptable maximum
    :return: valid integer size or Exception if impossible
    """

    valid_size = type_cast(size)
    if least_value is not None and valid_size < least_value:
        raise ValueError

    if largest_value is not None and valid_size > largest_value:
        raise ValueError

    return valid_size


def validate_range(type_cast, lesser, greater, *args,
                   lower_bound=None, upper_bound=None):
    """
    Validates range
    :param type_cast:
    :param lesser: string, supposed to be lower bound
    :param greater: string, supposed to be upper bound

    :param lower_bound:
    :param upper_bound:
    :return: tuple that is range of values
    """
    a, b = type_cast(lesser), type_cast(greater)

    if args:
        raise TypeError

    if lower_bound is None:
        lower_bound = a

    if upper_bound is None:
        upper_bound = b

    # sifting nan's
    if a != a or b != b:
        raise TypeError

    # sifting invalid range order
    elif not lower_bound <= a <= b <= upper_bound:
        raise ValueError

    else:
        return a, b


def validate_file_path(file_path):
    """
    Validates filename or its path to the filename
    :param file_path: path to the file
    :return: validated path to the file or exception if not found
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError
    else:
        return file_path

