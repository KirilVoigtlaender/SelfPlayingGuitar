

# Create your views here.
from django.shortcuts import render, redirect
from .forms import FileForm
from .models import File
import os

def file_selection(request):
    files = File.objects.all()
    form = FileForm()

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_selection')

    return render(request, 'file_selection.html', {'form': form, 'files': files})

def read_file(request, file_id):
    file_obj = File.objects.get(pk=file_id)
    file_path = file_obj.path.path

    # Perform file reading operations here
    with open(file_path, 'r') as file:
        content = file.read()

    return render(request, 'read_file.html', {'content': content})
