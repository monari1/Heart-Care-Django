from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),



    # path('register/', views.register.as_view(), name='register'),
    # path('login/', views.login_view.as_view(), name='login'),
]