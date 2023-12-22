#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2023  <guitar@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from adafruit_servokit import ServoKit
import time
import mido
#import pigpio

def map_midi_into_letter(midi_notes):
    notes = ["A2","A#2","B2","C3","C#3","D3","D#3","E3","F3","F#3","G3","G#3","A3","A#3","B3","C4","C#4","D4","D#4"]
    if midi_notes-45 >=0 and midi_notes-45 < 19:
        return notes[midi_notes-45]

    # if midi_notes == 57:
    #     return "A3"
    # elif midi_notes == 67:
    #     return "G4"
    # elif midi_notes == 62:
    #     return "D4"
        

        
def map_midi_to_server(note, kit):
    if note == "A2":
        # kit.servo[0].angle = 20
        # time.sleep(1)
        # kit.servo[0].angle = 140
        return (0,0)
    elif note == "D3":
        # kit.servo[1].angle = 20
        # time.sleep(1)
        # kit.servo[1].angle = 140
        return (0,1)
    elif note == "G3":
        # kit.servo[2].angle = 20
        # time.sleep(1)
        # kit.servo[2].angle = 140
        return (0,2)
    elif note == "D#3":
        return (1,1)        
    elif note == "E3":
        return (2,1)
    elif note == "G#3":
        return (1,2)
    elif note == "A3":
        return (2,2)
    


def fret_string(string, position, kit):
    servonumber = string + position//2 + 2
    if(position%2 == 1):
        kit.servo[servonumber].angle = 60
        time.sleep(1)
        kit.servo[servonumber].angle = 90
    else:
        kit.servo[servonumber].angle = 120
        time.sleep(1)
        kit.servo[servonumber].angle = 90

def pluck_string(string, kit):
    if(kit.servo[string].angle == 140):
        kit.servo[string].angle = 20
    else:
        kit.servo[string].angle = 140

def play_strings(fin, kit):
    string_is_playing = [False,False,False]
    
    for message in fin.play():
        if message.type  in ['note_on']:
            note = map_midi_into_letter(message.note)
            position, string = map_midi_to_server(note)
            if string_is_playing[string] == False:
                string_is_playing[string] = True
                fret_string(string,position,kit)
                pluck_string(string,kit)
                string_is_playing[string] = False

def main(args):
    #file_path = file_field.path
    kit = ServoKit(channels=16)
    #file = Midi_file . 
    #fin = mido.MidiFile(file)
    fin = mido.MidiFile("some.mid")
    # for message in fin.play():
    #     if message.type in ['note_on', 'note_off']:
    #         outgoing_letter = map_midi_into_letter(message.note)
    #         outgoing_turned_servo = map_midi_to_server(outgoing_letter,kit)
    play_strings(fin,kit)
    return 0
    

    


    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    

