import mido
from adafruit_servokit import ServoKit
from .midi_functions.map_midi_into_letter import map_midi_into_letter
from .midi_functions.map_midi_to_server import map_midi_to_server
from .midi_functions.play_strings import play_strings
from .models import File
def playing(file_field):
    file_path = file_field.path
    kit = ServoKit(channels=16)
    #file = Midi_file . 
    #fin = mido.MidiFile(file)
    fin = mido.MidiFile(file_path)
    play_strings(fin,kit)
    
    return 0
