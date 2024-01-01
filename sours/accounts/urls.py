from django.urls import path
from accounts.views import logout_view
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import RegisterView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='user_create')
    ]