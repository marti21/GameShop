from django.shortcuts import render, redirect
from .models import Game
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

def show_error_404(request, exception):
    if request.user.is_authenticated:
        return render(request, '404.html', status=404)
    else:
        return redirect('login')


def loginUser(request):
    form = AuthenticationForm(data=request.POST)

    if request.user.is_authenticated:
        return redirect('trends')
    
    if form.is_valid():
        user = form.get_user()

        login(request, user)
        #messages.success(request,'LOGGGIIINN')
        return redirect('trends')

    return render(request, 'login.html', {'form':form})


@login_required(login_url='login/')
def get_trend_games(request):
    games = Game.objects.filter(trend=True)

    context = {
        'games' : games
    }

    return render(request, 'trends.html', context)

@login_required(login_url='login/')
def get_game(request, gameName):
    print('Va a buscar el juego')
    game = get_object_or_404(Game, name=gameName)
    print(game)

    context = {
        'game' : game
    }

    return render(request, 'game.html', context)

@login_required(login_url='login/')
def game_list(request):
    games_list = Game.objects.filter(trend=True).order_by('name')
    paginator = Paginator(games_list, 3)  # Aquí especificamos que queremos mostrar 10 elementos por página

    page = request.GET.get('page')
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un entero, mostrar la primera página.
        games = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera del rango (página vacía), mostrar la última página.
        games = paginator.page(paginator.num_pages)

    return render(request, 'games.html', {'games': games})