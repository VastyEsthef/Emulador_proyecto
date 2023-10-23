from django.urls import path
from django.contrib.auth.views import LogoutView
from . views import lista_mvs, crear_mv, eliminar_mv, logueo, registro


urlpatterns = [
   path('',lista_mvs.as_view(), name='mvs'),
   path('login/', logueo.as_view(), name='login'),
   path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
   path('registro/', registro.as_view(), name='registro'),
   path('crear-mv/', crear_mv.as_view(), name='crear-mv'),
   path('eliminar-mv/<int:pk>', eliminar_mv.as_view(), name='eliminar-mv'),
   
]