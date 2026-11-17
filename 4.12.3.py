hiver = ["décembre", "janvier", "février"]
printemps = ["mars", "avril", "mai"]
ete = ["juin", "juillet", "août"]
automne = ["septembre", "octobre", "novembre"]
saisons = [hiver, printemps, ete, automne]

print(saisons[2])
print(saisons[1][0])
print(saisons[1:2])
print(saisons[:][1])

#mois = hiver+printemps+ete+automne
mois = sum(saisons, [])
print(mois[5])