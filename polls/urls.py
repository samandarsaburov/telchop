from django.urls import path
from .views import (get_all, index, Delete, Updete, Create)

urlpatterns = [
    path('get/', get_all.as_view()),
    path('index/<int:id>',index.as_view()),
    path('del/<int:id>', Delete.as_view()),
    path('update/<int:id>', Updete.as_view()),
    path('create/', Create.as_view())
]
