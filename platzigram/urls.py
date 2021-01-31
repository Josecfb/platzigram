"""Prueba de hola mundo """
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from platzigram import views as local_views
from posts import views as post_views
from users import views as user_views



urlpatterns = [
    path('admin/',admin.site.urls),
    
    path('hola/', local_views.hola),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),
    
    path('',post_views.list_posts, name="feed"),
    path('posts/new/',post_views.create_post,name="create_post"),
    
    path('users/login/',user_views.login_view, name="login"),
    path('users/logout/',user_views.logout_view, name="logout"),
    path('users/signup',user_views.signup_view, name="signup"),
    path('users/me/profile',user_views.update_profile, name='update_profile')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
