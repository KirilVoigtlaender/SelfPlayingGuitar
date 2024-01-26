import json
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.template import loader
from .models import File
from .forms import FileForm
from .playing import playing
from django.shortcuts import redirect


def delete(request):
    return render(request, 'Delete/delete.html')
def edit(request):
    return render(request, 'Edit/edit.html')
def play(request):
    return render(request, 'Play/play.html')


## File ##
def delete_list(request):
    return render(request, 'Delete/delete_file.html', {
        'delete_list': File.objects.all(), #Update the key to 'delete_list'
    })
    
## File ##
def edit_list(request):
    return render(request, 'Edit/edit_file.html', {
        'edit_list': File.objects.all(), #Update the key to 'edit_list'
    })
    
## File ##
def play_list(request):
    return render(request, 'Play/play_file.html', {
        'play_list': File.objects.all(), #Update the key to 'play_list'
    })



## Adding the files ##
# We check if the newly added name/file combination is valid and if it is we render it with the file_form.html in the add folder
def add_file(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'Add/file_form.html', {'form': FileForm}) 


## Editing files ##
# This can alow the user to edit the name and/or the file itself
def edit_file(request, pk):
    file = get_object_or_404(File, pk=pk)
    form = FileForm(instance=file)

    if request.method == 'POST':
        form = FileForm(request.POST, instance=file)
        if form.is_valid():
            form.save()
            # Redirect to the edit list view after saving changes
            return redirect('edit')
    return render(request, 'Edit/edit_form.html', {'form': form, 'file': file})

## Playing files ##
# If you press on a file yo be played it will call the playing function with the path of the newly selected file by the user
def play_file(request, pk):
    file = get_object_or_404(File, pk = pk)
    playing(file.path)
    return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "FileListChanged": None,
                        "showMessage": f"{file.name} played."
                    })
                }
            )

## Deleting files ##
# Here we make sure that the file is also removed from your device/ doesn't appear in the media folder anymore after you decided to delete it.
# For that we again get a file and then use the integrated os extension to gain acces to the device and delete it also locally.     
@ require_POST
def remove_file(request, pk):
    file = get_object_or_404(File, pk=pk)
    if file.path:
        file_path = file.path.path
        if os.path.isfile(file_path):
            os.remove(file_path)
    file.delete()
    return render(request,'Delete/delete_file.html')

## This view sets up the website ##
def website(request):
    return render(request, 'website.html')
