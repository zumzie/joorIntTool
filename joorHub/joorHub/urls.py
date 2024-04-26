from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', include('uploadTool.urls')),
    path('accounts/', include('accounts.urls')),
    path('', views.home, name='home'),
    path("__reload__/", include("django_browser_reload.urls"))
]
