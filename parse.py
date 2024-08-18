
# takes Account list, Format must be one line per Account Details (Example: mynameislol:TeSt)


def parseInputList():
    print(1)
    lines = []
    while True:
        user_input = input()
        if user_input == '':
            break
        else:
            lines.append(user_input)
    return lines


# text must be string containing Name and password, separated only by a ":" with no spaces

def parseAccountData(text):
    text = list(text)
    PW = []
    while True:
        try:
            val = text.pop()
            if val == ":":
                break
            PW.insert(0, val)
        except:
            print("blocked")
            break
    return [("".join(text)), "".join(PW)]

def parseLevelText(text):
    t = list(text)
    del t[0:3]
    return "".join(t)
