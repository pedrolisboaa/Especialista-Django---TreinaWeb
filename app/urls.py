from django.urls import path
from .views import ClienteCreateView

urlpatterns = [
   
    path("index", ClienteCreateView.as_view()),
]
