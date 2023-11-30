from django.urls import path
from browser import views

urlpatterns = [
    path("", views.principal, name="home"),
    path("'resultados/'", views.resultados, name='resultados'),
]