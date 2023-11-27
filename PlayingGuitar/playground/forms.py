from django import forms

SONGCHOICES= [
    ('sonata_1_1__c_iscenko.mid', 'sonata_1_1__c_iscenko.mid')
]

class Song_choice_form(forms.Form):
    song_choice = forms.FileField(label= 'Choose a song.', widget= forms.Select(choices=SONGCHOICES))