import time
def fret_string(string, position, kit):
    servonumber = string + position//2 + 2
    if(position%2 == 1):
        kit.servo[servonumber].angle = 20
        time.sleep(1)
        kit.servo[servonumber].angle = 80
    else:
        kit.servo[servonumber].angle = 140
        time.sleep(1)
        kit.servo[servonumber].angle = 80