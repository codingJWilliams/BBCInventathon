#import libary to read keypresses
import msvrct
#import libary to show images
from PIL import Image
#import random number generation libary
from random import randint
#import time
import time
#create a function to simplify showing images
def show_image(image_location):
  image = Image.open(image_location)
  image.show()
#read the current keypress and save it to the input_char variable
input_char=msvrct.getch()
#save the fruit names to the relevant charcaters the makey makey will send
orange='1'
bannana='2'
lemon='3'
lime='4'
#save current cpu time in the start_time variable
start_time=time.time()
#while current time minus start tiem is less than or equal to 60
while time.time()-start_time<=60:
  #save a randomly generated number between 0 and 12 to the number variable
  number=randint(0,12)
  #if number equal 0 then
  if number==0:
    #while input_char variable isn't equal to the lemon variable
    while input_char!=lemon:
      #show_image
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
