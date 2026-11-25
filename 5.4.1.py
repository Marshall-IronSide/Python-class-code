liste= ["vache", "souris", "levure", "bacterie"]

print("Avec la boucle for")
for i in range(len(liste)):
    print(f"{liste[i]}")

print("Avec la boucle while")
i=0
while i<len(liste):
    print(f"{liste[i]}")
    i=i+1