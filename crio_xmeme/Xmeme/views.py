from django.http.response import Http404, JsonResponse
from django.shortcuts import render, redirect
from .forms import memesForm
from .models import memes

# Create your views here.

# memes list 
def memes_List(request):
    context = {'memes_List' : memes.objects.all().order_by('-id') }
    return render(request, "Xmeme/memes_List.html",context)

# memes forms
def memes_form(request, id=0):
    try:
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
    except memes.DoesNotExist:
        raise Http404('Page not found')

# memes delete options
def memes_delete(request, id):
    meme = memes.objects.get(pk=id)
    meme.delete()
    return redirect('/memes')

# memes json for particular id
def memes_json(request, id):
    context = {
        'meme_list': memes.objects.filter(pk=id),
    }
    return render(request, "Xmeme/memes_json.html", context)
    