import sys, termios, tty, os, time
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
button_delay = 0.2
 
while True:
    char = getch()
 
    if (char == "w"):
        print("Bannana")
        time.sleep(button_delay)
 
    elif (char == "s"):
        print("Lime")
        time.sleep(button_delay)
 
    elif (char == "d"):
        print("Orange")
        time.sleep(button_delay)
 
    elif (char == "a"):
        print("Lemon")
        time.sleep(button_delay)
