from .map_midi_into_letter import map_midi_into_letter
from .map_midi_to_servo import map_midi_to_servo
from .fret_string import fret_string
from .unfretstring import unfret_string
from .pluck_string import pluck_string
import mido
import time
def play_strings(fin, kit):
    # Take in a file and play the guitar
    fin.ticks_per_beat = fin.ticks_per_beat
    ticks_per_beat = fin.ticks_per_beat
    
    for message in fin.play():
        ticks = message.time
        waiting_time = mido.tick2second(ticks,ticks_per_beat,500000)
        time.sleep(waiting_time)
        if message.type  in ['note_on']:
            if message.note-45 >=0 and message.note-45 < 19:
                note = map_midi_into_letter(message.note)
                string, fret = map_midi_to_servo(note)
                fret_string(string,fret,kit)
                time.sleep(0.3)
                pluck_string(string,kit)
                time.sleep(0.3)
                unfret_string(string,fret,kit)
                time.sleep(0)
