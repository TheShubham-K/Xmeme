from django.shortcuts import render, redirect
from .forms import memesForm
from .models import memes

# Create your views here.

def memes_List(request):
    context = {'memes_List' : memes.objects.all() }
    return render(request, "Xmeme/memes_List.html",context)

def memes_form(request, id=0):
    if request.method == 'GET':
        if id==0:
            form = memesForm()
        else:
            meme = memes.objects.get(pk=id)
            form = memesForm(instance=meme)    
        return render(request, "Xmeme/memes_form.html", {'form': form})
    else:
        if id == 0:
            form = memesForm(request.POST)
        else:
            meme = memes.objects.get(pk=id)
            form = memesForm(request.POST,instance=meme)
        if form.is_valid():
            form.save()
        return redirect('/memes')

def memes_delete(request, id):
    meme = memes.objects.get(pk=id)
    meme.delete()
    return redirect('/memes')
