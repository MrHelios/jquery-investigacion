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

def ejemplos_set(request):
    return render(request, 'HTML/set.html')

def ejemplos_add(request):
    return render(request, 'HTML/add.html')

def manipular_css(request):
    return render(request, 'HTML/m_css.html')

def manipular_css_II(request):
    return render(request, 'HTML/m_css_II.html')

def dim_wid_hei(request):
    return render(request, 'HTML/dimension-1.html')

def dim_innwid_innhei(request):
    return render(request, 'HTML/dimension-2.html')

def parent(request):
    return render(request, 'HTML/parent.html')

def upload_basico(request):
    return render(request, 'HTML/upload-basico.html')
