N= 5

tab = []
i=0

for i in range(N):
    tab.append(int(input("number : ")))


s=0

for iteam in tab:
    s=s+iteam

print("somme :" + str(s) )
print("moyen : " + str( float(s)/N) )
