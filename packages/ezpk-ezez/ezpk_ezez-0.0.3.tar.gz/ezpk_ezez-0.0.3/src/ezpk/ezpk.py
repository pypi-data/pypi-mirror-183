def dic(mn,mx,li):
    def _dic(num,w):
        lll = ""
        ff = 0
        if num >9:
            raise ValueError('max num too big')
        if num == 1:
            s = len(w)
            s = 100/s
            for a in w:
                ff += s
                print("1:",int(ff),"%")
                lll += a
                lll += "\n"
        if num == 2:
            s = len(w)
            s = 100/s
            for a in w:
                ff += s
                print("2:",int(ff),"%")
                for b in w:
                    lll += a+b
                    lll += "\n"
        if num == 3:
            s = len(w)
            s = 100/s
            for a in w:
                ff += s
                print("3:",int(ff),"%")
                for b in w:
                    for c in w:
                        lll += a+b+c
                        lll += "\n"
        if num == 4:
            s = len(w)
            s = 100/s
            for a in w:
                ff += s
                print("4:",int(ff),"%")
                for b in w:
                    for c in w:
                        for d in w:
                            lll += a+b+c+d
                            lll += "\n"
        if num == 5:
            s = len(w)
            s = 100/s
            for a in w:
                ff += s
                print("5:",int(ff),"%")
                for b in w:
                    for c in w:
                        for d in w:
                            for e in w:
                                lll += a+b+c+d+e
                                lll += "\n"
        if num == 6:
            s = len(w)
            s = 100/s
            for a in w:
                ff += s
                print("6:",int(ff),"%")
                for b in w:
                    for c in w:
                        for d in w:
                            for e in w:
                                for f in w:
                                    lll += a+b+c+d+e+f
                                    lll += "\n"
        if num == 7:
            s = len(w)
            s = 100/s
            for a in w:
                ff += s
                print("7:",int(ff),"%")
                for b in w:
                    for c in w:
                        for d in w:
                            for e in w:
                                for f in w:
                                    for g in w:
                                        lll += a+b+c+d+e+f+g
                                        lll += "\n"
        if num == 8:
            s = len(w)
            s = 100/s
            for a in w:
                ff += s
                print("8:",int(ff),"%")
                for b in w:
                    for c in w:
                        for d in w:
                            for e in w:
                                for f in w:
                                    for g in w:
                                        for h in w:
                                            lll += a+b+c+d+e+f+g+h
                                            lll += "\n"
        if num == 9:
            s = len(w)
            s = 100/s
            for a in w:
                ff += s
                print("9:",int(ff),"%")
                for b in w:
                    for c in w:
                        for d in w:
                            for e in w:
                                for f in w:
                                    for g in w:
                                        for h in w:
                                            for i in w:
                                                lll += a+b+c+d+e+f+g+h+i
                                                lll += "\n"
        return lll
    ggg = ""
    nn = 0
    try:
        m = mn+mx+1
    except:
        raise TypeError('min/max must be type"int"')
    j = mx-mn+1
    j = 100/j
    for x in range(mn,mx+1):
        nn += j
        ggg += _dic(x,li)
        print("zzzzzddddd:",int(nn),"%")
    return ggg
if __name__ == "__main__":
    f = open(r'F:\desktop\3333.txt','w')
    f.write(zd(1,4,"1234567890"))
    f.close()
