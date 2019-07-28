from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from vkontakte_users.models import User


@login_required
def MainView(request):
    User.remote.fetch(ids=[1, 2, 6])
    user = User.remote.fetch(ids=[70911700])[0]
    return render(request,'vk/main.html', {'tu':user})