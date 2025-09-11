from pytamaro import *
rectangle_rouge = rectangle(320, 320, rgb_color(255, 0, 0))
rectangle_blanc_1 = rectangle(192, 64, rgb_color(255, 255, 255))
rectangle_blanc_2 = rectangle(64, 192, rgb_color(255, 255, 255))
drapeau_1 = (overlay(rectangle_blanc_1, rectangle_rouge))
drapeau_final = (overlay(rectangle_blanc_2, drapeau_1))

show_graphic(drapeau_final)
