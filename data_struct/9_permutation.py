def permutation(s):
    if len(s) < 2:
        return s
    res = []
    for i, c in enumerate(s):
        for cc in permutation(s[:i]+s[i+1:]):
            res.append(c + cc)
    return res


if __name__ == "__main__":
    data = "012"
    print(permutation(data))
