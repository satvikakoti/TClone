from django.urls import path
from .views import main_view, video_view, join_view

urlpatterns = [
    path('', main_view, name='main_view'),
    path('join/', join_view, name='join_view'),
    path('video/', video_view, name='video_view'),
]
