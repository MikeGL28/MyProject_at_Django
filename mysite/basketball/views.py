from django.shortcuts import render, redirect, get_object_or_404
from .models import BasketballGame, Player
from .forms import BasketballGameForm, PlayerForm
import calendar
from datetime import datetime


def basketball_profile(request):
    now = datetime.now()
    year = now.year
    month = now.month

    games = BasketballGame.objects.all().order_by('-date')
    players = Player.objects.all()

    # Генерация календаря
    calendar_data = get_calendar_data(year, month)

    # Среднее по играм
    total_games = games.count()
    avg_points = round(sum(game.total_points for game in games) / total_games, 2) if total_games else 0

    month_name = calendar.month_name[month]

    return render(request, 'basketball/basketball_profile.html', {
        'games': games,
        'players': players,
        'avg_points': avg_points,
        'calendar': calendar_data,
        'now': now,
        'month_name': month_name
    })

def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basketball:basketball_profile')
    else:
        form = PlayerForm()

    return render(request, 'basketball/add_player.html', {'form': form})


def add_basketball_game(request):
    all_players = Player.objects.all()
    if request.method == 'POST':
        form = BasketballGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('basketball:basketball_profile')
    else:
        form = BasketballGameForm()

    return render(request, 'basketball/add_basketball_session.html', {
        'form': form,
        'all_players': all_players
    })


def edit_basketball_session(request, pk):
    session = get_object_or_404(BasketballGame, pk=pk)
    if request.method == 'POST':
        form = BasketballGameForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('basketball:basketball_profile')
    else:
        form = BasketballGameForm(instance=session)
    return render(request, 'edit_basketball_session.html', {'form': form})


def get_calendar_data(year, month):
    cal = calendar.Calendar()
    days_in_month = cal.itermonthdays(year, month)

    # Получаем все игры за этот месяц
    games = BasketballGame.objects.filter(date__year=year, date__month=month)
    game_dates = {game.date.day for game in games}

    data = []
    for day in days_in_month:
        if day == 0:
            data.append({'day': '', 'level': 0})  # Пустые дни
        else:
            intensity = 1 if day in game_dates else 0
            data.append({'day': day, 'level': intensity})

    return data


def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'basketball/player_detail.html', {'player': player})