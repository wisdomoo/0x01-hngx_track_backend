from django.urls import path
from api.views import get_info1,get_info

urlpatterns = [
    path('', get_info1, name='get_info1'),
    path('', get_info, name='get_info'),
    
]
