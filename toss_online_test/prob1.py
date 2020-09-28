def isValid(string):
    if set(string) != {"1", "2"}:
        return False

    for (idx, char) in enumerate(string):
        # we don't have to check last character
        if char == "1":
            try:
                assert(string[idx+1]=="2")
            except:
                return False

    return True


print(isValid("11"))
print(isValid("12"))
print(isValid("121"))
print(isValid("122"))
print(isValid("113"))
print(isValid(""))
print(isValid("a"))