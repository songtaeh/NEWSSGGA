from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, ProfileForm, LoginForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings

# Create your views here.

def signup(request):
    if request.method == 'POST':
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            user_instance = registerform.save(commit=False)
            user_instance.set_password(registerform.cleaned_data['password1'])
            user_instance.is_active = True
            user_instance.save()
            user=User.objects.get(username=registerform.cleaned_data['username'])
            auth.login(request, user,
                       backend='django.contrib.auth.backends.ModelBackend')
            return redirect('update_profile')
        else:
            registerform = RegisterForm(request.POST)
            return render(request, 'registration/signup.html', {'RegisterForm': registerform})

    registerform = RegisterForm()
    return render(request, 'registration/signup.html',{'RegisterForm':registerform})

def update_profile(request):
    user = request.user
    profile = user.profile
    
    profileform = ProfileForm(request.POST or None, request.FILES, instance=profile)

    context = {'profileform': profileform,
                    'profile': profile}

    if request.method == 'POST':
        if profileform.is_valid():
            profile.save()  
            return redirect('mainpage')
        
        else:
            return render(request, 'registration/update_profile.html', context)

            
    profileform = ProfileForm(instance=profile)
    context = {'profileform': profileform, 'profile':profile}
    

    return render(request, 'registration/update_profile.html', context)


class login(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        if not self.request.user.profile.name:    
            url = "/update_profile"
            return url
        else:
        # 로그인한 현재 페이지로 연결
            # url = self.request.path
            url = "/"
            return url
        
        return resolve_url(settings.LOGIN_REDIRECT_URL)
   
def login(request):
    return render(request, 'login.html')