from django.shortcuts import render, redirect
from AppCoder.models import Curso


# Create your views here.

def mostrar_cursos(request):
    curso = Curso.objects.all()
    contexto = {
        "cursos": curso,
        "nombre": "Stefano"
    }
    return render(request, "AppCoder/cursos.html", contexto)

def crear_curso(request):
    curso = Curso(nombre="Python", camada=477878)
    curso.save()
    return redirect("/app/cursos/")

def show_html(request):
    curso = Curso.objects.first()
    contexto = {"cursos": curso}
    return render(request, 'index.html', contexto)



