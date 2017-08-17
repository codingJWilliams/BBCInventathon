import msvrct
import time
#fruit mapping you may need to change this
orange='1'
bannana='2'
lemon='3'
lime='4'
input_char=msvrct.getch()
print("Please note that you may need to tweak the fruit mapping in this code and main.py")
print("Please tap the fruit to check the mapping")
start_time=time.time()
while start_time-time.time()<=15:
  if input_char==orange:
    print("Orange")
  elif input_char==bannana:
     print("Bannana")
  elif input_char==lemon:
    print("Lemon")
  elif input_char==lime:
    print("Lime")
print("Creating setup files") 
Bestscore=open("bestscore.txt","w")
  #write 0 to the best score file
  Bestscore.write("0")
  Bestscore=open("bestscorer.txt","w")
  #find the current time form the cpu and save it to the start_time variable
  #write nothing to the bestscorer fiel but still create it
  Bestscorer.write("")
  Bestscore.close()
  Bestscorer.close()