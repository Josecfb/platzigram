from django.urls import path
from django.views.generic import TemplateView

from users import views

urlpatterns = [
    path(route='<str:username>/'
         ,view=TemplateView.as_view(template_name='users/detail')
         ,name='detail'),
    path(route='login/',view=views.login_view, name="login"),
    path('logout/',views.logout_view, name="logout"),
    path('signup',views.signup_view, name="signup"),
    path('me/profile',views.update_profile, name='update_profile')
]
