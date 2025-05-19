from django.shortcuts import render, redirect, get_object_or_404
from .models import Training
from .forms import TrainingForm

def training_list(request):
    trainings = Training.objects.all().order_by('date')

    # Генерация данных для календаря
    import calendar
    from datetime import datetime

    now = datetime.now()
    _, days_in_month = calendar.monthrange(now.year, now.month)

    calendar_days = []

    # Словарь дат из тренировок
    training_dict = {training.date.day: training.intensity for training in trainings if training.date.month == now.month}

    for day in range(1, days_in_month + 1):
        intensity_level = training_dict.get(day, 0)  # 0 — нет данных
        calendar_days.append({
            'day': day,
            'level': intensity_level
        })

    context = {
        'trainings': trainings,
        'calendar': calendar_days,
        'month_name': now.strftime('%B')
    }

    return render(request, 'training_list.html', context)


def add_training(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workout:training_list')
    else:
        form = TrainingForm()

    return render(request, 'add_training.html', {'form': form})


def edit_training(request, pk):
    training = get_object_or_404(Training, pk=pk)
    if request.method == 'POST':
        form = TrainingForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect('workout:training_list')
    else:
        form = TrainingForm(instance=training)
    return render(request, 'edit_training.html', {'form': form})