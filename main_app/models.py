from django.db import models
from django.urls import reverse

# Frequency choices
DAILY = 1
WEEKLY = 2
MONTHLY = 3
FREQUENCY_CHOICES = (
    (DAILY, 'Daily'),
    (WEEKLY, 'Weekly'),
    (MONTHLY, 'Monthly'),
)

class Habit(models.Model):
    name = models.CharField(max_length=100)
    target = models.PositiveIntegerField(default=1)
    frequency = models.IntegerField(choices=FREQUENCY_CHOICES, default=DAILY)
    description = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('habit_detail', kwargs={'habit_id': self.id})

class DailyRecord(models.Model):
    habit = models.ForeignKey('main_app.Habit', on_delete=models.CASCADE)
    date = models.DateField()
    completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.habit.name} - {self.date}"
