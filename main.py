#import libary to read keypresses
import msvrct
#import libary to show images
from PIL import Image
#import libary to kill process showing image
import psutil
#import random number generation libary
from random import randint
#import time
import time
from time import sleep
#import libaries to flush stdout buffer and kill the process running the code
from sys import exit,stdout
#create a function so only one line is required for showing images
def show_image(image_location):
  image = Image.open(image_location)
  image.show()
#create function for clsoing image
def close_image():
  #Finds pid of process showing image
  for proc in psutil.process_iter():
    if proc.name() == "display":
      #Then drives an axe through it's heart!
      proc.kill()
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
program_start_time=time.time()
try:
  #open bestscore.txt in read mode
  Bestscore = open('bestscore.txt','r') 
  #open bestscorer.txt in read mode
  Bestscorer = open('bestscorer.txt','r') 
  #if Bestscore is blank
  if Bestscore.read()=="":
    #raise a FileNotFoundError as it might aswell not exist in it's current state
    raise FileNotFoundError
  #if the best scorer.txt file is empty
  elif Bestscorer.read()=="":
    #open bestscore.txt in write mode
     Bestscorer = open('bestscorer.txt','w')
     #Write the text no one
     Bestscorer.write("No one")
     #open bestscorer.txt in read mode
     Bestscorer = open('bestscorer.txt','r') 
      #store the contents of the bestscore.txt file in the bestscore variable
    bestscore=Bestscore.read()
    #store the contents of the bestscorer.txt file in the bestscorer variable
    bestscorer=Bestscorer.read()
    #tell the user the current bestscore and who it is by
    print("The best score is ",bestscore,"by",bestscorer)
  else:
    #store the contents of the bestscore.txt file in the bestscore variable
    bestscore=Bestscore.read()
    #store the contents of the bestscorer.txt file in the bestscorer variable
    bestscorer=Bestscorer.read()
    #tell the user the current bestscore and who it is by
    print("The best score is ",bestscore,"by",bestscorer)
  #while current time minus start tiem is less than or equal to 60
  while time.time()-program_start_time<=60:
    #save a randomly generated number between 0 and 12 to the number variable
    number=randint(0,12)
    #if number equals 0 then
    if number==0:
      start_time=time.time()
      #while time since start_time was saved is less than or equal to 3 seconds
      while start_time-time.time<=3:
        #while the inputed character is not equavilant to the lemon variable
        while input_char!=lemon:
          #show image
          show_image("/assets/bannana-lemon.png")
        #add one to score
        score=score+1
      #close image by finding pid of process showing image and then killing it
      close_image()
    elif number==1:
      start_time=time.time()
      while start_time-time.time<=3:
        while input_char!=lime:
          show_image("/assets/bannana-lime.png")
        score=score+1
      close_image
    elif number==2:
      start_time=time.time()
      while start_time-time.time<=3:
        while input_char!=orange:
          show_image("/assets/bannana-orange.png")
        score=score+1
      close_image()
    elif number==3:
      start_time=time.time()
      while start_time-time.time<=3:
        while input_char!=bannana:
          show_image("/assets/lemon-bannana.png")
        score=score+1
      close_image()
    elif number==4:
      start_time=time.time()
      while start_time-time.time<=3:
        while input_char!=lime:
          show_image("/assets/lemon-lime.png")
        score=score+1
      close_image()
    elif number==5:
      start_time=time.time()
      while start_time-time.time<=3:
        while input_char!=orange:
          show_image("/assets/lemon-orange.png")
        score=score+1
      close_image()
    elif number==6:
      start_time=time.time()
      while start_time-time.time<=3:
        while input_char!=bannana:
          show_image("/assets/orange-bannana.png")
        score=score+1
      close_image()
    elif number==7:
      start_time=time.time()
      while start_time-time.time<=3:
        while input_char!=lemon:
          show_image("/assets/orange-lemon.png")
        score=score+1
      close_image()
    elif number==8:
      start_time=time.time()
      while start_time-time.time<=3:
        while input_char!=lime:
          show_image("/assets/orange-lime.png")
          score=score+1
      close_image()
    elif number==9:
      start_time=time.time()
      while start_time-time.time<=3:
        while input_char!=bannana:
          show_image("/assets/lime-bannana.png")
        score=score+1
      close_image()
    elif number==10:
      start_time=time.time()
      while start_time-time.time<=3:
        while input_char!=lemon:
          show_image("/assets/lime-lemon.png")
        score=score+1
      close_image()
    elif number==11:
      start_time=time.time()
      while start_time-time.time<=3:
        while input_char!=orange:
          show_image("/assets/lime-orange.png")
        score=score+1
      close_image()
    #sleep to give cpu rest    
    sleep(0.05)
  #tell the user their score
  print("You scored",score)
  #convert the bestscore variable to an integer
  bestscore=int(bestscore)
  #if the score is greater than the bestscore
  if score>bestscore:
    #ask for the users name and save it in the name variable
    name=input("What's your name? ")
    #open the bestscore text file in write mode
    Bestscore=open("bestscore.txt","w")
    #write the score to the bestscore text file
    Bestscore.write(str(score))
    #close the text file to advoid errors when we next try and open it and to free up the cpu and ram
    Bestscore.close()
    #open the bestscorer text file in write mode
    Bestscorer=open("bestscorer.txt","w")
     #write the contents of the name variable to the bestscorer text file
    Bestscorer.write(str(name))
    #close the text file to advoid errors when we next try and open it and to free up the cpu and ram
    Bestscorer.close()
  
  else:
    #close the text file to advoid errors when we next try and open it and to free up the cpu and ram
    Bestscore.close()
    #close the text file to advoid errors when we next try and open it and to free up the cpu and ram
    Bestscorer.close()
#if the we get a File not found error
except FileNotFoundError:
  #tell the user that some files could not be found so we are cretang the neceray files
  print("Files could not be found:Creating files now")
  #
  Bestscore=open("bestscore.txt","w")
  #write 0 to the best score file
  Bestscore.write("0")
  Bestscore=open("bestscorer.txt","w")
  #find the current time form the cpu and save it to the start_time variable
  #write nothing to the bestscorer fiel but still create it
  Bestscorer.write("")
  #tell them the files have now been created and to restart the program
  print("Files created please start the program again")
   #close the text file to advoid errors when we next try and open it and to free up the cpu and ram
  Bestscore.close()
   #close the text file to advoid errors when we next try and open it and to free up the cpu and ram
  Bestscorer.close()
#in the unlikely event a user presses ctrl+c in order to quit the game
except Keyboard Interrupt:
  #flush the stdout buffer
  stdout.flush()
  #get the process runing this code to commit suicide
  exit()
