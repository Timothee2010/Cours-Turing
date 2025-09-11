from pytamaro import *
rectangle_bleu = rectangle(150, 300, rgb_color(0, 0, 145))
rectangle_blanc = rectangle(150, 300, rgb_color(255, 255, 255))
rectangle_rouge = rectangle(150, 300, rgb_color(255, 0, 15))
drapeau_1 = (beside(rectangle_bleu, rectangle_blanc))
drapeau_final = (beside(drapeau_1, rectangle_rouge))

show_graphic(drapeau_final)
