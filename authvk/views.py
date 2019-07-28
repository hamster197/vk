import vk
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.



#@login_required
def MainView(request):
    # profiles = vk.api.friends.get(user_id='70911700', order='hints')#self.id
    session = vk.AuthSession(app_id='6452474', user_login=self.login, user_password=self.password,
                             scope=['offline', 'messages', 'friends'])
    api = vk.API(session, v='5.62')
    api.friends.get(user_id=self.id, order='hints')
    return render(request,'vk/main.html',{'t':api})