import vk
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.



#@login_required
def MainView(request):
    # profiles = vk.api.friends.get(user_id='70911700', order='hints')#self.id
    # session = vk.Session()
    # vk_api = vk.API(session)
    # p = vk_api.users.get(user_id=1)
    return render(request,'vk/main.html',)#{'t':p})