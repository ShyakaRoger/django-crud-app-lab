from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Habit paths
    path('habits/', views.habit_index, name='habit_index'),
    path('habits/create/', views.HabitCreate.as_view(), name='habit_create'),
    path('habits/<int:habit_id>/', views.habit_detail, name='habit_detail'),
    path('habits/<int:pk>/update/', views.HabitUpdate.as_view(), name='habit_update'),
    path('habits/<int:pk>/delete/', views.HabitDelete.as_view(), name='habit_delete'),

    # DailyRecord add path
    path('habits/<int:habit_id>/add_record/', views.add_record, name='add_record'),
]
