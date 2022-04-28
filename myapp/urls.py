from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('getresource/', views.getresource, name='resources'),
   path('getmeeting/', views.getmeeting, name='meetings'),
   path('meetingview/<int:id>', views.meetingview, name='details'),

]