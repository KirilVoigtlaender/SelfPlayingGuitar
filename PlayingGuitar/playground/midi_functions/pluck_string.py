def pluck_string(string, kit):
    if(kit.servo[string].angle == 140):
        kit.servo[string].angle = 20
    else:
        kit.servo[string].angle = 140