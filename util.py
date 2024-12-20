def matrix_print(m):
    s = ""
    mm = 0
    for l in m:
        for e in l:
            ll = len(str(e))
            if ll > mm:
                mm = ll
    
    for l in m:
        for e in l:
            s  += f"{e:{mm}}"
        s += "\n"
    print(s[:-1])