from email import message
from hashlib import new
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Message, room

# Create your views here.

def home(request):
    return render(request,'home.html')

def room_func(request,room_name):
    username=request.GET.get('username')
    room_details=room.objects.get(room_name=room_name)
    return render(request,'room.html',{
        'username':username,
        'room_details':room_details,
        'room_name':room_name    
    })


def checkroom(request):

    room_name=request.POST['room_name']
    username=request.POST['username']

    if room.objects.filter(room_name=room_name).exists():
        return redirect('/'+room_name+'/?username='+username)
    else:
        new_room=room.objects.create(room_name=room_name)
        new_room.save()
        return redirect('/'+room_name+'/?username='+username)

def send(request):
    username=request.POST['username']
    message=request.POST['message']
    room_id=request.POST['room_id']

    new_message=Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully.')

def getMessages(request,room_name):
    room_details=room.objects.get(room_name=room_name)
    print(room_details)

    messages=Message.objects.filter(room=room_details.id)
    return JsonResponse({'messages':list(messages.values())})

