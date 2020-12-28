from django.shortcuts import render,redirect
from gestionMenus.models import Menus
from django.contrib import messages

# Create your views here.

def menus(request):

    if request.method == 'POST':
        entrada = request.POST['entrada']
        fondo = request.POST['fondo']
        postre = request.POST['postre']
        precio = request.POST['precio']

        menu = Menus(entrada=entrada,fondo=fondo,
                    postre=postre,precio=precio)
        menu.save()
        
        menus = Menus.objects.all()

        messages.add_message(request,messages.SUCCESS,"Menu guardado con exito")
        
        return render(request,'index.html',{'menus':menus})
    
    else:
        menus = Menus.objects.all()
        
    return render(request,'index.html',{'menus':menus,'cuenta':1})
    
def deleteMenu(request,idmenu):

    menu = Menus.objects.get(id=idmenu)
    menu.delete()

    menus = Menus.objects.all()

    messages.add_message(request,messages.ERROR,"Menu Eliminado con exito")
    return redirect('/menu/')


def editmenu(request,idmenu):
    menu = Menus.objects.get(pk=idmenu)
    return render(request,'updatemenu.html',{'menu':menu})

def updatemenu(request,idmenu):
    if request.method == 'POST':
        entrada = request.POST['entrada']
        fondo = request.POST['fondo']
        postre = request.POST['postre']
        precio = request.POST['precio']

        menu = Menus.objects.get(pk=idmenu)

        menu.entrada = entrada
        menu.save()

        menu.fondo = fondo
        menu.save()

        menu.postre = postre
        menu.save()

        menu.precio = precio
        menu.save()
        messages.add_message(request,messages.INFO,"Menu actualizado con exito")
        return redirect('/menu/')

