import mido
from adafruit_servokit import ServoKit
from .midi_functions.play_strings import play_strings

def playing(file_field):
    # Read file from path 'file_field' and play this file on the guitar.
    file_path = file_field.path
    kit = ServoKit(channels=16)

    fin = mido.MidiFile(file_path)
    play_strings(fin,kit)
    
    return 0
