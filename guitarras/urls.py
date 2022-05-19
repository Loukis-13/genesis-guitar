from django.urls import path

from . import views


app_name = 'guitarras'
urlpatterns = [
    path('', views.index, name='index'),
    path('guitarras', views.index, name='guitarras'),
    path('guitarras/editar', views.editar, name='editar'),
    path('guitarras/salvar', views.salvar, name='salvar'),
]