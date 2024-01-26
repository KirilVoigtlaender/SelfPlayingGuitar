def pluck_string(string, kit):
    # Turn the servo to pluck a string
    if(139 <= kit.servo[string].angle <= 141):
        kit.servo[string].angle = 20
        print("string", string)
    else:
        kit.servo[string].angle = 140
        print("string", string)
