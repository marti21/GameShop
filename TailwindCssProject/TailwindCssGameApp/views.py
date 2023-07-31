from django.shortcuts import render, redirect
from .models import Game
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect


def loginUser(request):
    form = AuthenticationForm(data=request.POST)

    if request.user.is_authenticated:
        return redirect('games')
    
    if form.is_valid():
        user = form.get_user()

        login(request, user)
        messages.success(request,'LOGGGIIINN')
        return redirect('games')

    return render(request, 'login.html', {'form':form})


@login_required(login_url='/')
def get_all_games(request):
    games = Game.objects.all()

    context = {
        'games' : games
    }

    return render(request, 'games.html', context)
