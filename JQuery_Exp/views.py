from django.shortcuts import render

def index(request):
    return render(request, 'HTML/index.html')

def ejemplos_fade(request):
    return render(request, 'HTML/fade.html')

def ejemplos_slide(request):
    return render(request, 'HTML/slide.html')

def ejemplos_animate(request):
    return render(request, 'HTML/animate.html')

def ejemplos_stop(request):
    return render(request, 'HTML/stop.html')

def ejemplos_cadena(request):
    return render(request, 'HTML/cadena.html')
