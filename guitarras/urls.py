from django.urls import path

from . import views


app_name = 'guitarras'
urlpatterns = [
    path('', views.GuitarraListaView.as_view(), name='index'),
    path('guitarras', views.GuitarraListaView.as_view(), name='guitarras'),
    path('guitarras/criar', views.CriarGuitarraView.as_view(), name='criar'),
    path('guitarras/editar/<pk>', views.EditarGuitarraView.as_view(), name='editar'),
    path('guitarras/excluir/<pk>', views.ExcluirGuitarraView.as_view(), name='excluir'),
]
