def quick_sort(iterable):
    """
    Quicksort algorithm function
    :param iterable: iterable to be sorted
    :return: sorted iterable(initial remains unaffected)
    """
    # nothing to sort
    if len(iterable) <= 1:
        return iterable

    # split list by pivot
    else:
        pivot = iterable[len(iterable) // 2]

        # universal iterable constructors
        cls = type(iterable)

        lesser = cls.__new__(cls)
        equal = cls.__new__(cls)
        greater = cls.__new__(cls)

        lesser.__init__()
        equal.__init__()
        greater.__init__()

        # TypeError can be raised if elements are incomparable
        for element in iterable:
            if element < pivot:
                lesser.append(element)
            elif element == pivot:
                equal.append(element)
            else:
                greater.append(element)

        # sort sub-lists and return sorted
        return quick_sort(lesser) + equal + quick_sort(greater)
