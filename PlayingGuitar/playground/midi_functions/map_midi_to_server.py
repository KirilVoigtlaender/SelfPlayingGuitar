import time
def map_midi_to_server(note, kit):
    if note == "A2":
        kit.servo[0].angle = 20
        time.sleep(1)
        kit.servo[0].angle = 140
        return 0
    elif note == "D3":
        kit.servo[1].angle = 20
        time.sleep(1)
        kit.servo[1].angle = 140
        return 1
    elif note == "G3":
        kit.servo[2].angle = 20
        time.sleep(1)
        kit.servo[2].angle = 140
        return 2