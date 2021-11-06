
def compterMots(texte):
    d = {}
    Words = texte.split()

    for mot in Words:
        if mot in d:
            d[mot] = d[mot] + 1
        else:
            d[mot] = 1

    return d

dict = compterMots("ayoub cherguelaine is the best bnadem f denya ayoub")

for c in dict.keys():
    print(c, ":", dict[c])