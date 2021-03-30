from django.shortcuts import render, redirect
from .models import administracion
from django.http import HttpResponse
from .forms import formularioForm

# Create your views here.

def general(request):
    general=administracion.objects.all()
    ctx={
       'general':general
    }

    return render(request, "general.html", ctx)

def registrar(request):
    ctx={
        'form':formularioForm()
    }
    if request.method == 'POST':
        formulario=formularioForm(request.POST)
        if formulario.is_valid():
           formulario.save()
           ctx['notificacion']="EL USUARIO SE HA REGISTRADO CORRECTAMENTE"
        return redirect('general')
    return render(request, "registrar.html", ctx)



def modificar(request, id):
    administrar = administracion.objects.get(id=id)
    ctx={
        'form':formularioForm(instance=administrar)
    }
    if request.method =='POST':
        formulario = formularioForm(data=request.POST, instance=administrar)
        if formulario.is_valid():
           formulario.save()

           ctx['notificacion']="EL USUARIO SE HA MODIFICADO CORRECTAMENTE"
           ctx['from']=formulario
        return redirect('general')
    return render(request, "modificar.html", ctx)
    

def eliminar(request, id):
    administrar = administracion.objects.get(id=id)
    administrar.delete()
    return redirect('general')
    return HttpResponse("USUARIO ELIMINADO CORRECTAMENTE")



	


