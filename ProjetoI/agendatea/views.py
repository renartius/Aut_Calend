from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect
from agendatea.forms import CompromissoForm

def home(request):
    return HttpResponse("Agenda TEA")

def criar_compromisso(request):
    if request.method == 'POST':
        form = CompromissoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_compromissos')
    else:
        form = CompromissoForm()
    return render(request, 'compromissos/criar_compromisso.html', {'form': form})

def listar_compromissos(request):
    compromissos = Compromisso.objects.all()
    return render(request, 'compromissos/listar_compromissos.html', {'compromissos': compromissos})

