from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm
from django.utils import timezone

def calendario(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendario')
    else:
        form = TarefaForm()

    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/calendario.html', {'form': form, 'tarefas': tarefas})


def home(request):

    return HttpResponse('Calendário TEA')
