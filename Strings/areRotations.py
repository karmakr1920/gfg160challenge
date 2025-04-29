def areRotations(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_concat = s1 + s1
    return s2 in s1_concat
print(areRotations('abcd','cdab'))