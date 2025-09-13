from pytamaro import*

def eye(color):
  part3 = ellipse(90,90, white)
  part2 = ellipse(30,30, color)
  part1 = ellipse(20,20, black)
  return

def eyes(color):
  single_eye = eye(color)
  space = rectangle(10,10, transparent)
  return beside(single_eye, beside(space, single_eye))

def person(head_color, eye)
