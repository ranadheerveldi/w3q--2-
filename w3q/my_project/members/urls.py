from django.urls  import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('add/', views.add_member, name='add_member'),
    path('success/', views.success, name='success'),
    path('login/',views.login_view, name ='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),



]
