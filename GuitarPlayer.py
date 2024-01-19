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

def fret_string(string, fret, kit):
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
    
    if(left_right == 1):
        if(servonumber== 14 or servonumber ==11 or servonumber ==8 or servonumber == 5):
            kit.servo[servonumber].angle = 87
        else:
            kit.servo[servonumber].angle = 75
    elif(left_right == 2):
        if(servonumber== 14 or servonumber ==11 or servonumber ==8 or servonumber == 5):
            kit.servo[servonumber].angle = 117
        else:
            kit.servo[servonumber].angle = 105
    print(servonumber)


def pluck_string(string, kit):
    # print(kit.servo[string].angle)
    if(139 <= kit.servo[string].angle <= 141):
        kit.servo[string].angle = 20
        print("string", string)
    else:
        kit.servo[string].angle = 140
        print("string", string)

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




    

def play_strings(fin, kit):
    fin.ticks_per_beat = fin.ticks_per_beat
    ticks_per_beat = fin.ticks_per_beat
    #string_is_playing = [False,False,False,True]
    
    for message in fin.play():
        ticks = message.time
        waiting_time = mido.tick2second(ticks,ticks_per_beat,500000)
        time.sleep(waiting_time)
        if message.type  in ['note_on']:
            if message.note-45 >=0 and message.note-45 < 19:
                note = map_midi_into_letter(message.note)
                string, fret = map_midi_to_server(note,kit)
            #if string_is_playing[string] == False:
                #string_is_playing[string] = True
                fret_string(string,fret,kit)
                time.sleep(0.3)
                pluck_string(string,kit)
                time.sleep(0.3)
                unfret_string(string,fret,kit)
                time.sleep(0)
            
                #print(note)
                #print(time.time())
                
                
                #string_is_playing[string] = False

def main(args):
    #file_path = file_field.path
    kit = ServoKit(channels=16)

    #fin = mido.MidiFile('/home/guitar/Desktop/New Devices/Project/c14/sonata_1_1__c_iscenko.mid')
    #for message in fin.play():
     #   if message.type in ['note_on', 'note_off']:
      #      outgoing_letter = map_midi_into_letter(message.note)
       #     outgoing_turned_servo = map_midi_to_server(outgoing_letter,kit)
    #kit.servo[0].angle = 110
    #kit.servo[1].angle = 60
    

    #file = Midi_file . 
    #fin = mido.MidiFile(file)
    fin = mido.MidiFile('/home/guitar/Desktop/New Devices/Project/c14/sonata_1_1__c_iscenko.mid')
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
    

