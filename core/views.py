from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Pessoa

def minha_view(request):
    pessoas = Pessoa.objects.all()

    data = {
        'pessoas': [
            {'id': pessoa.id, 'nome': pessoa.nome}
            for pessoa in pessoas
        ]
    }

    return JsonResponse(data)

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html",{"pessoas":pessoas})

def salvar(request):
   vnome = request.POST.get("nome")
   Pessoa.objects.create(nome=vnome)
   pessoas = Pessoa.objects.all()
   return render(request,"index.html",{"pessoas":pessoas})

def editar(request,id):
   pessoa = Pessoa.objects.get(id=id)
   return render(request,"update.html",{"pessoa":pessoa})  

def update(request,id):
   vnome = request.POST.get("nome")
   pessoas = Pessoa.objects.get(id=id)
   pessoas.nome = vnome
   pessoas.save()
   return redirect(home)

def delete(request, id):
    pessoas = Pessoa.objects.get(id=id)
    pessoas.delete()
    return redirect(home)