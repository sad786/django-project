from django.shortcuts import render
from . import models
# Create your views here.

def show_list(req):
    notes_list = models.Notes.objects.all()
    return render(req,'notes/note_list.html',{'notes':notes_list})

