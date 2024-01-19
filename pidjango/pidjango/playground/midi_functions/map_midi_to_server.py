import time
def map_midi_to_server(note, kit):
    # returns string, fret   based on note
    something = True
    if note == "A2":
        return 0,0
    elif note == "A#2":
        return 0, 1
    elif note == "B2":
        return 0,2
    elif note == "C3":
        return 0,3
    elif note == "C#3":
        return 0,4
    elif note == "D3":
        if something:
            return 0,5 
        else:
            return 1,0 
    elif note == "D#3":
        if something:
            return 0,6 
        else:
            return 1,1 
    elif note == "E3":
        if something:
            return 0,7  
        else:
            return 1,2 
    elif note == "F3":
        if something:
            return 0,8  
        else:
            return 1,3 
    elif note == "F#3":
        return 1,4
    elif note == "G3":
        if something:
            return 1,5  
        else:
            return 2,0 
    elif note == "G#3":
        if something:
            return 1,6  
        else:
            return 2,1 
    elif note == "A3":
        if something:
            return 1,7  
        else:
            return 2,2 
    elif note == "A#3":
        if something:
            return 1,8  
        else:
            return 2,3 
    elif note == "B3":
        return 2,4
    elif note == "C4":
        return 2,5
    elif note == "C#4":
        return 2,6
    elif note == "D4":
        return 2,7
    elif note == "D#4":
        return 2,8
    return 3,0
