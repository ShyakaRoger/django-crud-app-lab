from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Habit
from .forms import HabitForm, RecordForm

# Home view
def home(request):
    return render(request, 'habits/home.html')

# About page
def about(request):
    return render(request, 'habits/about.html')

# Habit index page
def habit_index(request):
    habits = Habit.objects.all()
    return render(request, 'habits/index.html', {'habits': habits})

# Habit detail page
def habit_detail(request, habit_id):
    habit = Habit.objects.get(id=habit_id)
    record_form = RecordForm()
    return render(request, 'habits/detail.html', {
        'habit': habit,
        'record_form': record_form
    })

# Add daily record
def add_record(request, habit_id):
    form = RecordForm(request.POST)
    if form.is_valid():
        new_record = form.save(commit=False)
        new_record.habit_id = habit_id
        new_record.save()
    return redirect('habit_detail', habit_id=habit_id)

# Create habit
class HabitCreate(CreateView):
    model = Habit
    form_class = HabitForm
    template_name = 'habits/habit_form.html'

# Update habit
class HabitUpdate(UpdateView):
    model = Habit
    form_class = HabitForm
    template_name = 'habits/habit_form.html'

# Delete habit
class HabitDelete(DeleteView):
    model = Habit
    success_url = '/habits/'
    template_name = 'habits/habit_confirm_delete.html'
