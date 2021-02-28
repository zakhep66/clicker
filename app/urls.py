from django.urls import path
from . import views
from app.views import *


urlpatterns = [
    path('', views.index, name='mainPage'),
    path('owner/detial/<int:pk>', OwnerDetailView.as_view()),
]