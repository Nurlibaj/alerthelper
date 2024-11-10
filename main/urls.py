from django.contrib import admin
from django.urls import path, include
from . import views
from .views import EventCreateView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path('', views.index,name='index'),
    path('create-event/', EventCreateView.as_view(), name='create-event'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
