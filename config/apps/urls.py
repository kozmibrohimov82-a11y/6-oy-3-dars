from django.urls import path
from .views import index,about,info


urlpatterns = [
    path('',index),
    path('about/',about),
    path('info/',info),
]
