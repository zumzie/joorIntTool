from django.urls import path
from .views import upload_home
from .views import upload_file_view

urlpatterns = [
    path('', upload_home, name='upload_tool'),
    path('file/', upload_file_view, name='upload_file'),
]
