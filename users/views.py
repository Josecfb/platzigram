"""Users view"""
# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.urls import reverse

#Models
from django.contrib.auth.models import User
from posts.models import Post
#Forms
from users.forms import ProfileForm, SignupForm

class UserDetailView(LoginRequiredMixin,DetailView):
    template_view='users/detail.html'
    slug_field='username'
    slug_url_kwarg='username'
    queryset=User.objects.all()
    context_object_name='user'
    
    def get_context_data(self,**kwargs):
        """añador posts al contexto"""
        context=super().get_context_data(**kwargs)
        user=self.get_object()
        context['posts']=Post.objects.filter(user=user).order_by('-created')
        return context


def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,'users/login.html',{'error':'Invalid username or password'})
    return render(request,'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=SignupForm()
    return render(request,'users/signup.html',{'form':form})

@login_required
def update_profile(request):
    profile=request.user.profile
    if request.method=='POST':
        form=ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data=form.cleaned_data
            profile.website=data['website']
            profile.phone_number=data['phone_number']
            profile.biography=data['biography']
            profile.picture=data['picture']
            profile.save()
            url=reverse('detail',kwargs={'username':request.user.username})
            return redirect(url)
    else:
        form=ProfileForm()
    profile = request.user.profile
    return render(request,'users/update_profile.html',context={
                                                        'profile':profile,
                                                        'user':request.user,
                                                        'form':form
                                                    })

