from django.urls import path
from adminapp.views import BidsView, EditBidsView, UserListView, EditUserView

urlpatterns = [
    path('<int:page>/', BidsView.as_view(), name='staff_profile'),
    path('users/<int:page>/', UserListView.as_view(), name='staff_user_list'),
    path('edit/<int:pk>/', EditBidsView.as_view(), name='staff_edit_bid'),
    path('user/<int:pk>/', EditUserView.as_view(), name='staff_edit_user'),

]
