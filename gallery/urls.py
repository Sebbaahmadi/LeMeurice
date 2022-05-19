from django.urls import path
from . import views

urlpatterns = [
    path('prod', views.prod, name='prod'),
    # {Changed the name of the function from contact to Contact because of the function we changed}
]