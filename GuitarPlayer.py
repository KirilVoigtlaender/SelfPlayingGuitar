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
    if midi_notes == 57:
        return "A3"
    elif midi_notes == 67:
        return "G4"
    elif midi_notes == 62:
        return "D4"
        
        
def map_midi_to_server(note,kit):
    if note == "A3":
        kit.servo[0].angle = 20
        time.sleep(1)
        kit.servo[0].angle = 140
        return 0
    elif note == "D4":
        kit.servo[1].angle = 20
        time.sleep(1)
        kit.servo[1].angle = 140
        return 1
    elif note == "G4":
        kit.servo[2].angle = 20
        time.sleep(1)
        kit.servo[2].angle = 140
        return 2
        
def main(args):
    #pi = pigpio.pi()
    kit = ServoKit(channels=16)
    fin = mido.MidiFile('/home/guitar/Desktop/New Devices/Project/c14/sonata_1_1__c_iscenko.mid')
    for message in fin.play():
        if message.type in ['note_on', 'note_off']:
            outgoing_letter = map_midi_into_letter(message.note)
            outgoing_turned_servo = map_midi_to_server(outgoing_letter,kit)
    


    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    

