from pytamaro import *

### couleur Mille-Feuille
couleur_glacage = rgb_color(210, 194, 185)
couleur_pate = rgb_color(156, 98, 33)
couleur_creme = rgb_color(231, 205, 122)

### forme mille feuille avec couleur
pate = rectangle(300, 5, couleur_pate)
creme = rectangle(300, 10, couleur_creme)
patisserie = rectangle(300, 10, couleur_glacage)

etage_to_do = 21
mille_feuille = rectangle(0, 0, transparent)
while etage_to_do > 0:
    mille_feuille = above(creme, above(pate, mille_feuille))
    etage_to_do -= 2

mille_feuille = above(patisserie, above(pate, mille_feuille))


save_graphic('mille-feuille.png', mille_feuille)
