from django.urls import path
from .views import main,index

urlpatterns = [
    # path('', main.main, name=""),
    path('', index.index, name="index"),
]