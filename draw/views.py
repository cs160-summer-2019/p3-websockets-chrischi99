from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'draw/index.html', {})

  
def small_screen(request):
    return render(request, 'draw/small_screen.html', {})
  
def recording(request):
    return render(request, 'draw/recording.html', {})
 
def small_screen_2(request):
    return render(request, 'draw/small_screen_2.html', {})