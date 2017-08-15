import msvrct
import Image
def show_image(image_location):
  image = Image.open(image_location)
  image.show()
input_char=msvcrt.getch()
if input_char.upper()=='W':
  print("Strawberry")
if input_char.upper()=='A':
  print("Bannana")
  if input_char.upper()=='S':
  print("Lemon")
  if input_char.upper()=='D':
  print("Melon")
