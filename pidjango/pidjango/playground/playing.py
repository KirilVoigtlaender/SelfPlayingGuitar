import mido
from adafruit_servokit import ServoKit
from .midi_functions.map_midi_into_letter import map_midi_into_letter
from .midi_functions.map_midi_to_server import map_midi_to_server
from .models import File
def playing(file_field):
    file_path = file_field.path
    kit = ServoKit(channels=16)
    #file = Midi_file . 
    #fin = mido.MidiFile(file)
    fin = mido.MidiFile(file_path)
    for message in fin.play():
        if message.type in ['note_on', 'note_off']:
            outgoing_letter = map_midi_into_letter(message.note)
            outgoing_turned_servo = map_midi_to_server(outgoing_letter,kit)
    
    return 0
