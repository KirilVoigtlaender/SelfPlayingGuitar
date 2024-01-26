def map_midi_into_letter(midi_note):
    # Return the name of the note that corresponds with the midi number 'midi_note'
    notes = ["A2","A#2","B2","C3","C#3","D3","D#3","E3","F3","F#3","G3","G#3","A3","A#3","B3","C4","C#4","D4","D#4"] # All playable notes
    if midi_note-45 >=0 and midi_note-45 < 19:
        return notes[midi_note-45]