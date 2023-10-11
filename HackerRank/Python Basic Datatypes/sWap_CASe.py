def swap_case(s):
    c =[]
    for i in s:
        if(i == i.upper()):
            i = i.lower()
            c.append(i)
        else:
            i = i.upper()
            c.append(i)
    c = "".join(c)
    return c

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)