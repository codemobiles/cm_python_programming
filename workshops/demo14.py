# Arbitrary Argument, *args

def test(printAll: bool, *courses):
    if printAll:
        for c in courses:
            print(c)
    else:
        print(courses[0])


test(False, "Angular", "React", "Vue",)
