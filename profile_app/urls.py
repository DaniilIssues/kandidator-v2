from django.urls import path
from profile_app.views import bid_list_in_work_view, create_bid, bid_list_in_archive_view, stop_work, play_work, EditBidView

urlpatterns = [
    path('work/<int:pk>/page/<int:page>/', bid_list_in_work_view, name='bids_list_work'),
    path('archive/<int:pk>/page/<int:page>/', bid_list_in_archive_view, name='bids_list_archive'),
    path('create/<int:pk>/', create_bid, name='create'),
    path('edit/<int:pk>/', EditBidView.as_view(), name='edit'),
    # path('edit/<int:pk>/', edit_ajax, name='edit'),
    path('stop/<int:pk>/', stop_work, name='stop_work'),
    path('play/<int:pk>/', play_work, name='play_work'),
]