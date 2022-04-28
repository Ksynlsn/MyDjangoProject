from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')


def getresource(request):
    resource_list=Resource.objects.all()
    return render(request, 'myapp/resources.html', {'resource_list' : resource_list})


def getmeeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'myapp/meetings.html', {'meeting_list' : meeting_list})


def meetingview(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'myapp/meetingview.html', {'meeting' : meeting})