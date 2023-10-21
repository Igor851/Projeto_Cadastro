from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms

def index(request):
    alunos = models.Aluno.objects.all()
    return render(request, 'index.html', {'alunos':alunos})

def aluno(request, id):
    aluno = get_object_or_404(models.Aluno, id=id )
    return render(request, 'aluno.html', {'aluno':aluno})

def form(request):
    form=forms.AlunoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        return render(request, 'form.html', {'form':form})