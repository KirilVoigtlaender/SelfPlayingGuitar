

# # Create your views here.
# from django.shortcuts import render, redirect
# from .forms import FileForm
# from .models import File
# import os

# def file_selection(request):
#     files = File.objects.all()
#     form = FileForm()

#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('file_selection')

#     return render(request, 'file_selection.html', {'form': form, 'files': files})

# def read_file(request, file_id):
#     file_obj = File.objects.get(pk=file_id)
#     file_path = file_obj.path.path

#     # Perform file reading operations here
#     with open(file_path, 'r') as file:
#         content = file.read()

#     return render(request, 'read_file.html', {'content': content})

# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FileForm  # Replace with your actual form
from .models import File
import mido
from adafruit_servokit import ServoKit
from .midi_functions.map_midi_into_letter import map_midi_into_letter
from .midi_functions.map_midi_to_server import map_midi_to_server

def file_selection(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            selected_file_id = request.POST.get('selected_file')
            selected_file = File.objects.get(id=selected_file_id)
            play_selected_file(selected_file.path)
            return HttpResponse("File is being played.")
    else:
        form = FileForm()

    files = File.objects.all()
    return render(request, 'file_selection.html', {'form': form, 'files': files})

def play_selected_file(file_path):
    kit = ServoKit(channels=16)
    fin = mido.MidiFile(file_path)
    for message in fin.play():
        if message.type in ['note_on', 'note_off']:
            outgoing_letter = map_midi_into_letter(message.note)
            outgoing_turned_servo = map_midi_to_server(outgoing_letter, kit)
