#import libary to read keypresses
import msvrct
#import libary to show images
from PIL import Image
#import liabry to kill process showung image
import psutil
#import random number generation libary
from random import randint
#import time
import time
from time import sleep
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
#set score to 0
score=0
#save current cpu time in the start_time variable
start_time=time.time()
#while current time minus start tiem is less than or equal to 60
while time.time()-start_time<=60:
  #save a randomly generated number between 0 and 12 to the number variable
  number=randint(0,12)
  #if number equals 0 then
  if number==0:
    #while input_char variable isn't equal to the lemon variable
    while input_char!=lemon:
      #show_image
      show_image("/assets/bannana-lemon.png")
    score=score+1
    #close image by finding pid of process showing image and then killing it
    for proc in psutil.process_iter():
      if proc.name() == "display":
        proc.kill()
  elif number==1:
    while input_char!=orange:
      show_image("/assets/bannana-orange.png")
    score=score+1
    for proc in psutil.process_iter():
      if proc.name() == "display":
        proc.kill()
  elif number==2:
    while input_char!=lime:
      show_image("/assets/bannana-lime.png")
    score=score+1
    for proc in psutil.process_iter():
      if proc.name() == "display":
        proc.kill()
  elif number==3:
    while input_char!=bannana:
      show_image("/assets/lemon-bannana.png")
    score=score+1
    for proc in psutil.process_iter():
      if proc.name() == "display":
        proc.kill()
  elif number==4:
    while input_char!=orange:
      show_image("/assets/lemon-orange.png")
    score=score+1
    for proc in psutil.process_iter():
      if proc.name() == "display":
        proc.kill()
  elif number==5:
    while input_char!=lime:
      show_image("/assets/lemon-lime.png")
    score=score+1
    for proc in psutil.process_iter():
      if proc.name() == "display":
        proc.kill()
  elif number==6:
    while input_char!=bannana:
      show_image("/assets/orange-bannana.png")
    score=score+1
    for proc in psutil.process_iter():
      if proc.name() == "display":
        proc.kill()
  elif number==7:
    while input_char!=lemon:
      show_image("/assets/orange-lemon.png")
    score=score+1
    for proc in psutil.process_iter():
      if proc.name() == "display":
        proc.kill()
  elif number==8:
    while input_char!=lime:
      show_image("/assets/orange-lime.png")
    score=score+1
    for proc in psutil.process_iter():
      if proc.name() == "display":
        proc.kill()
  elif number==9:
    while input_char!=bannana:
      show_image("/assets/lime-bannana.png")
    score=score+1
    for proc in psutil.process_iter():
      if proc.name() == "display":
        proc.kill()
  elif number==10:
    while input_char!=lemon:
      show_image("/assets/lime-lemon.png")
    score=score+1
    for proc in psutil.process_iter():
      if proc.name() == "display":
        proc.kill()
  elif number==11:
    while input_char!=orange:
      show_image("/assets/lime-orange.png")
    score=score+1
    for proc in psutil.process_iter():
      if proc.name() == "display":
        proc.kill()
  #sleep to give cpu rest    
  sleep(0.05)
