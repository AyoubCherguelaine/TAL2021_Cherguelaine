def d(x):

    if divmod(x,2)[1] == 0:
        print(" Ce nombre est pair")
    elif divmod(x,3)[1] ==0 :
        print("Ce nombre est impair et multiple de 3")
    else:
        print("Ce nombre n'est ni pair ni multiple de 3")





d(int(input("x  : ")))