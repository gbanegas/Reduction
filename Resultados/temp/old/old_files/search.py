
def search(degree):
    fileName = "pol_" + str(degree) + "_.txt"
    f = open(fileName, 'w')

    pols = []
    for i in xrange(0,degree):
        p = x**degree + x^i + 1
        if p.is_irreducible():
            f.write(str(p) + "\n")
            pols.append(p)

    if len(append) > 1:
        for i in xrange(0, degree):
            for j in xrange(i+1, degree):
                for h in xrange(h+1, degree):
                    p = x**degree + x**i + x**j + x**h + 1
                    if p.is_irreducible():
                        f.write(str(p) + "\n")
                        pols.append(p)

    f.close()
    print pols

