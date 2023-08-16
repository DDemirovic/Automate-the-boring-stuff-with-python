# ctrl + c = infinite loop stop (sorgt für "KeyboardInterrupt"
#continue/break:    break ist ein beenden des Vorgangs (Schleife/if bspw.)
#                   continue skippt den Rest im Block und springt zum Anfang zurück

# Aufgabe bei spam = 1 "Hello", spam = 2 "Howdy" und bei allen anderen Werten "greetings"
spam = -3
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Gretings')

# while i (maybe expression):
# for i in range(start, end, stepargument)

# Aufgabe: while Schleife benutzen um Zahlen von 1-10 zu printen
print('while loop')
i = 0
while i <10:
    i = i + 1
    print(i)
    
#Aufgabe: for Schleife benutzen um Zahlen von 1-10 zu printen
print('for loop')
for i in range(1,11,1):
    print(i)

# Ein Modul ist einfach eine Datei die python code enthält (wie diese hier).
# wenn man eine Datei benutzen möchte dann einfach import DATEINAME
# Bsp.: import beispiel
# Um nun eine Funktion aus "beispiel" aufzurufen einfach beispiel.funktionInBeispie
