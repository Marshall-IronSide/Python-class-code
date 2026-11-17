semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

# 1 - Tranches avec des indices positifs
print (semaine[:5])
print(semaine[5:])

# Même résultat avec des indices négatifs
print(semaine[:-2])
print(semaine[-2:])

# Dernier jour
print(semaine[6])
print(semaine[-1])

# Inverser la liste
print(semaine[::-1])
# Inverser la liste avec seulement les jours ouvrables
print(semaine[6::-1])