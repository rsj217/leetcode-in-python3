s = "egg"
t = "add"

s = "foo"
t = "bar"
#
# s = "paper"
# t = "title"
#
# s = "bbbaaaba"
# t = "aaabbbba"
#
# s="badc"
# t="xaxa"

def aaa(s, t):

    assert len(s) == len(t)
    dct = dict()
    used = []
    for i in range(len(s)):
        if s[i] not in dct:
            if t[i] in used:
                return False
            dct[s[i]] = t[i]
            used.append(t[i])
        else:
            if dct[s[i]] !=  t[i]:
                return False
    return True


ans = aaa(s, t)
print(ans)
