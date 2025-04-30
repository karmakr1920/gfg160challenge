def computeLPSArray(pat):
    lps = [0] * len(pat)
    length = 0
    i = 1
    while i < len(pat):
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def search(pat, txt):
    lps = computeLPSArray(pat)
    i = 0  # index for txt
    j = 0  # index for pat
    indices = []

    while i < len(txt):
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == len(pat):
            indices.append(i - j)
            j = lps[j - 1]  # corrected line

        elif i < len(txt) and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices

# print(search('ab','abcab'))
