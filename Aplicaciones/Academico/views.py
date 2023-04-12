from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

# Create your views here.

def home(request):
    cursos_listados = Curso.objects.all()
    messages.success(request, 'Cursos Listado correctamente')
    return render(request, "gestionCurso.html",{"cursos": cursos_listados})
 

    
def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    credito = request.POST['numCreditos']

    curso = Curso.objects.create(codigo = codigo, nombre=nombre, credito=credito)

    return redirect('/')

def edicion_curso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html",{"cursos": curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    credito = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.credito = credito
    curso.save()

    return redirect('/')


def eliminar_curso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    
    curso.delete()
    messages.success(request, 'Cursos Eliminado')

    return redirect('/')

