def unfret_string(string,fret,kit):
    servonumber = 3
    left_right = 0
    
    if(fret%2 == 1):
        left_right = 1
    else:
        left_right = 2
    if(fret == 1 or fret == 2):
        servonumber = 13 + string
    elif(fret == 3 or fret == 4):
        servonumber = 10 + string
    elif(fret == 5 or fret == 6):
        servonumber = 7 + string
    elif(fret == 7 or fret == 8):
        servonumber = 4 + string
    if(servonumber== 14 or servonumber ==11 or servonumber ==8 or servonumber == 5):
        kit.servo[servonumber].angle = 102 
    else:
        kit.servo[servonumber].angle = 90
    print("un", servonumber)
