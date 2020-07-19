from django.shortcuts import render, redirect
from .forms import *

def index(request):
    polls = Createpoll.objects.all()

    context = {'polls': polls}
    return render(request, 'namo/index.html', context)

def create(request):
    form = CreatepollForm()
    if request.method == "POST":
        form = CreatepollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'namo/create.html', context)

def vote(request, pk):
    quev = Createpoll.objects.get(id=pk)

    context = {'quev': quev}
    return render(request, 'namo/vote.html', context)

def result(request, pk):
    que = Createpoll.objects.get(id=pk)
    if request.method == "POST":
        selected = request.POST['option']
    if selected == que.opt1:
        que.vo1 += 1
        que.save()
    elif selected == que.opt2:
        que.vo2 += 1
        que.save()
    else:
        que.vo3 += 1
        que.save()

    context = {'que': que}
    return render(request, 'namo/result.html', context)

def viewresult(request, pk):
    que = Createpoll.objects.get(id=pk)
    context = {'que': que}
    return render(request, 'namo/result.html', context)

def delete(request, pk):
    poll = Createpoll.objects.get(id=pk)
    if request.method == "POST":
        poll.delete()
        return redirect('/')

    context = {'poll': poll}
    return render(request, 'namo/delete.html', context)

def intro(request):
    return render(request, 'namo/intro.html')

