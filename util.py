def matrix_print(m):
    s = ""
    for l in m:
        for e in l:
            s  += str(e)
        s += "\n"
    print(s[:-1])