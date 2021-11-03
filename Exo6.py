
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

val =int( input("number : "))

o =0

#print("val : " + str(val))

for i in range(10):
  #  print("t[i] : " + str(t[i]) + " and result : " +str( val == t[i]))
    if val == t[i]:
        o=o+1

if o == 0:
    print("no item")
else:
    print("'occurrence = " + str(o))
