from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('registration',views.registration,name='registration'),
    path('store_data',views.store_data,name='store_data'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('login_page',views.login_page,name='login_page'),
    # path('user_page',views.user_page,name='user_page'),

    
]