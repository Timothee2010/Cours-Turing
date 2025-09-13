from pytamaro import *

def entete(titre):
    label = text(titre, "Helvetica", 16, black)
    fond = rectangle(80, 80, rgb_color(240, 240, 240))
    return overlay(label, fond)


table = rectangle(0, 0, transparent)

liste = ["a", "b", "not a", "a and b", "a or b"]
for i in liste:
    carre = entete(i)
    table = beside(table, carre)

def case(valeur):
    label = text(str(valeur), "Helvetica", 16, black)
    if valeur:
        couleur_fond = green
    else:
        couleur_fond = red
    fond = rectangle(80, 80, couleur_fond)
    return overlay(label, fond)

liste_a = [False, True]
liste_b = [False, True]

for a in liste_a:
    for b in liste_b:
        print("valeur de not a", a or b)

save_graphic('Table-de-verite.png', table)
