from django import forms
from .models import Habit, DailyRecord

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'target', 'frequency', 'description']

class RecordForm(forms.ModelForm):
    class Meta:
        model = DailyRecord
        fields = ['date', 'completed', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3})
        }
