from pytamaro import *
def segment(numero, couleur_corps, couleur_patte):
 label = text(str(numero), "Helvetica", 16, black)
 label = pin(center, label)
 corps = ellipse(50, 50, couleur_corps)
 patte = ellipse(30, 30, couleur_patte)
 return above(overlay(label, corps), patte)

oeil = ellipse(30, 30, white)
oeil = overlay(ellipse(15, 15, black), oeil)
forme = ellipse(70, 70, blue)
forme = beside(ellipse(30, 30, red), forme)
forme = overlay(oeil, forme)

abdomen = rectangle(0, 0, transparent)

x = 1
while x <= 10:
    if x % 3 == 0:
        if x <= 4:
            new_segment = segment(x, yellow, blue)
            abdomen = beside(abdomen, new_segment)
            x += 1
        else:
            new_segment = segment(x, yellow, green)
            abdomen = beside(abdomen, new_segment)
            x += 1
    else:
        if x <= 4:
            new_segment = segment(x, red, blue)
            abdomen = beside(abdomen, new_segment)
            x += 1
        else:
            new_segment = segment(x, red, green)
            abdomen = beside(abdomen, new_segment)
            x += 1

forme = beside(forme, abdomen)
forme = beside(forme, ellipse(30, 30, black))
save_graphic('mille-pattes.png', forme)

abdomen = rectangle(0, 0, transparent)
