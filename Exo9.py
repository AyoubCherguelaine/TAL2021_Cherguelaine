d={'nom' : 'Ben', 'prenom' : 'Sama', 'age': 22}

d['prenom'] = 'sana'


print(d.keys())

print(d.values())

print(d)

st = d['prenom'] + ' ' + d['nom'] + ' a ' + str(d['age']) + ' ans '

print(st)
