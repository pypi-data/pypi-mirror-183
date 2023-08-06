def DictToList(d1, d2):
    # d1 = {"English": 100, "Maths": 56, "Science": 67, "Physics": 78}
    # d2 = {"English": 200, "Version": 500, "Syllabus": 9}
    a = set()
    for x in d1:
        a.add(x)
    for x in d2:
        a.add(x)
    ### Adding values and keys both ###
    b = set()
    for x, y in d1.items():
        a.add(x)
        b.add(y)
    for x, y in d2.items():
        a.add(x)
        b.add(y)
    print(a, b)
    l1 = []
    l2 = []
    l1.append(a)
    l1.append(b)
    l2.extend(a)
    l2.extend(b)
    print("Dict To List Response")
    print(l1)
    print(l2)

