from pytamaro import *
rectangle_noir = rectangle(450, 100, rgb_color(0, 0, 0))
rectangle_rouge = rectangle(450, 100, rgb_color(255, 0, 0))
rectangle_jaune = rectangle(450, 100, rgb_color(255, 204, 0))
drapeau_1 = (above(rectangle_noir, rectangle_rouge))
drapeau_final = (above(drapeau_1, rectangle_jaune))

show_graphic(drapeau_final)
