def MergeDictSameKey(d1, d2):
    for x in d2:
        y = d1[x] + d2[x]
        print(y)
        d1[x] = y
        print("Merge dictionary same key")
        print(d1)


def MergeDictDiffKey(d1, d2):
    for x in d1:
        if x in d2:
            d2[x] = d1[x] + d2[x]
            print(d2[x])
    d1.update(d2)
    print("Merge dictionary diff key")
    print(d1)
