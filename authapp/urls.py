from django.urls import path
from authapp.views import register, MyLoginView, ChangePassword, MyLogoutView

urlpatterns = [
    path('', register, name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('send_password/', ChangePassword.as_view(), name='send_password'),
]
