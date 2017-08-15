import msvcrt
import time

keystate = 'HIGH'
while True:
  if msvcrt.kbhit():
    msvcrt.getch()
    keystate = 'LOW'
  else:
    keystate = 'HIGH'
  # you may want to put a time.sleep() call here
  # to avoid eating up CPU
  time.sleep(0.1)
  print(keystate)
