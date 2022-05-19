from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    # {Changed the name of the function from contact to Contact because of the function we changed}
]