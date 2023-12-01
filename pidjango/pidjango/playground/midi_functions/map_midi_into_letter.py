def map_midi_into_letter(midi_notes):
    notes = ["A2","A#2","B2","C3","C#3","D3","D#3","E3","F3","F#3","G3","G#3","A3","A#3","B3","C4","C#4","D4","D#4"]
    return notes[midi_notes-45]

    # if midi_notes == 57:
    #     return "A3"
    # elif midi_notes == 67:
    #     return "G4"
    # elif midi_notes == 62:
    #     return "D4"