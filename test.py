animaux = ["vache", "souris", "levure", "bacterie"]

for animal in animaux:
 print(animal)
print('-------------------------------------------------')

for i in range (len(animaux)):
 print(animaux[i])
print('-------------------------------------------------')
i=0
while i < len(animaux):
 print(animaux[i])
 i=i+1

print('-------------------------------------------------')
i=-len(animaux)
while i < 0:
 print(animaux[i])
 i=i+1