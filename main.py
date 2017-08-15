import msvrct
import Image
from random import randint
def show_image(image_location):
  image = Image.open(image_location)
  image.show()
input_char=msvrct.getch()
strawberry='w'
bannana='a'
lemon='s'
melon='d'
while True:
  number=randint(0,12)
  if number==0:
    while input_char!=lemon:
      show_image("/assets/bannana-lemon.png")
  elif number==1:
    while input_char!=melon:
      show_image("/assets/bannana-melon.png")
  elif number==2:
    while input_char!=strawberry:
      show_image("/assets/bannana-strawberry.png")
  elif number==3:
    while input_char!=bannana:
      show_image("/assets/lemon-bannana.png")
  elif number==4:
    while input_char!=melon:
      show_image("/assets/lemon-melon.png")
  elif number==5:
    while input_char!=strawberry:
      show_image("/assets/lemon-strawberry.png")
  elif number==6:
    while input_char!=bannana:
      show_image("/assets/melon-bannana.png")
  elif number==7:
    while input_char!=lemon:
      show_image("/assets/melon-lemon.png")
  elif number==8:
    while input_char!=strawberry:
      show_image("/assets/melon-strawberry.png")
  elif number==9:
    while input_char!=bannana:
      show_image("/assets/strawberry-bannana.png")
  elif number==10:
    while input_char!=lemon:
      show_image("/assets/strawberry-lemon.png")
  elif number==11:
    while input_char!=melon:
      show_image("/assets/strawberry-melon.png")
  #sleep to give cpu rest    
  sleep(0.05)
