from django.urls import path
from main.apps import MainConfig
from main.views import PostCreateView

app_name = MainConfig

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),

]
