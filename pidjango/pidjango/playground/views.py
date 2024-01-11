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
from .functions import handle_uploaded_file

def index(request):
    #main view with the button
    return render(request, 'index.html')#The same as his index.html


def delete(request):
    return render(request, 'Delete/delete.html')
def edit(request):
    return render(request, 'Edit/edit.html')
def play(request):
    return render(request, 'Play/play.html')


## File ##
def delete_list(request):
    return render(request, 'Delete/delete_file.html', {
        'delete_list': File.objects.all(), #Update the key to 'file_list'
    })
    
## File ##
def edit_list(request):
    return render(request, 'Edit/edit_file.html', {
        'edit_list': File.objects.all(), #Update the key to 'file_list'
    })
    
## File ##
def play_list(request):
    return render(request, 'Play/play_file.html', {
        'play_list': File.objects.all(), #Update the key to 'file_list'
    })




def add_file(request):
    # form = FileForm()
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse (
            #         status= 204,
            #         headers ={
            #             'HX-Trigger': json.dumps({
            #             "FileListChanged": None,
            #             "showMessage": f"{form.name} added"
            #         })
            #     }
            # )
    return render(request, 'Add/file_form.html', {'form': FileForm}) 


# def edit_file(request, pk):
#     file = get_object_or_404(File, pk=pk)
#     form = FileForm(instance=file)  # Define an empty form instance
#     if request.method == 'POST':
#         form = FileForm(request.POST, instance=file)
#         if form.is_valid():
#             form.save()
#             return HttpResponse(
#                 status=204,
#                 headers={
#                     'HX-Trigger': json.dumps({
#                         "FileListChanged": None,
#                         "showMessage": f"{file.name} updated."
#                     })
#                 }
#             )
    #return render(request, 'Add/file_form.html', {'form': form})
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
    
@ require_POST
def remove_file(request, pk):
    file = get_object_or_404(File, pk=pk)
    if file.path:
        file_path = file.path.path
        if os.path.isfile(file_path):
            os.remove(file_path)
    file.delete()
    # return HttpResponse(
    #     status=204,
    #     headers={
    #         'HX-Trigger': json.dumps({
    #             "FileListChanged": None,
    #             "showMessage": f"{file.name} deleted."
    #         })
    #     })
    return render(request,'Delete/delete_file.html')

def website(request):
    return render(request, 'website.html')