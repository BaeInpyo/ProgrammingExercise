def isValid(a):
    """
    1. Try to partition a into left and right
    2. If both left and right is valid, answer is True
    """

    if not a:
        return "YES"

    left, right = partition(a[1:], a[0])
    print("a, left, right: {}, {}, {}".format(a, left ,right))
    if left is None and right is None:
        # cannot partition
        return "NO"

    return "YES" if (isValid(left) and isValid(right)) else "NO"

def partition(lst, key):
    """ Partition given list by key, return (left, right)
    If partition is not feasible, return (None, None)
    Left contains only smaller than keys, right contains only larger than key.
    """
    if not lst:
        return [], []

    index = None
    for idx in range(len(lst)):
        if lst[idx] > key:
            index = idx
            break

    if index is None:
        # all numbers in lst is smaller than key
        return lst, []

    left = lst[:index]
    right = lst[index:]
    for num in right:
        # cannot partition
        if num < key:
            return None, None

    return left, right


isValid([1,3,4,2])
