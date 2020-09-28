def isValid(string):
    try:
        numbers = [int(x) for x in string.split(" ")]
    except:
        return False

    # string must contain 6 distinct item
    if len(set(numbers)) != 6:
        return False

    # each item must be integer within [1, 45]
    for number in numbers:
        if not (1 <= number <= 45):
            return False

    # each item must be sorted order
    if numbers != sorted(numbers):
        return False

    return True

print(isValid("1 2 3 4 5 6"))
print(isValid("1 3 5 7 7 9"))
print(isValid("1 2 4 5 6"))
print(isValid("2 1 3 5 7 9"))
print(isValid("46 1 3 5 7 9"))
