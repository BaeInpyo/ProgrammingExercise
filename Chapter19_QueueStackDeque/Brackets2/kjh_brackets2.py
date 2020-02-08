pairs = {"}": "{", "]": "[", ")": "("}
def _f():
    st = []
    for c in input():
        if c in pairs:
            if not st or pairs[c] != st[-1]:
                return "NO"
            st.pop()
        else:
            st.append(c)
    return "NO" if st else "YES"


for _ in range(int(input())):
    print(_f())
