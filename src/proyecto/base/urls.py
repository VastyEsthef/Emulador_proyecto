from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
#from .views import landing_page
from .views import lista_mvs, crear_mv, eliminar_mv, logueo, registro
from .views import list_topologies, create_topology, detail_topology, delete_topology
from .views import list_vms, create_vm, link_vm

urlpatterns = [
   #--------------- Landing Page ---------------
   path('',views.landing_page, name='landing-page'),
   
   #-------------- Login / Registro ---------------
   path('login/', logueo.as_view(), name='login'),
   path('logout/', LogoutView.as_view(next_page = 'landing-page'), name='logout'),
   path('registro/', registro.as_view(), name='registro'),
   
   #-------------- Topo ---------------
   path('list-topo/',list_topologies.as_view(), name='topologies'),
   path('create-topo/', create_topology.as_view(), name='create-topology'),
   path('topology/<int:pk>', detail_topology.as_view(), name = 'topology'),
   path('delete-topo/<int:pk>', delete_topology.as_view(), name='delete-topology'),
   
   #-------------- Vm ---------------
   path('list-vm/',list_vms.as_view(), name='vms'),
   path('create-vm/', create_vm.as_view(), name='create-vm'),
   path('link-vm/', link_vm.as_view(), name='link-vm'),
   
   
   
   #-------------- Mv OLD ---------------
   path('listar-mv/',lista_mvs.as_view(), name='mvs'),
   path('crear-mv/', crear_mv.as_view(), name='crear-mv'),
   path('eliminar-mv/<int:pk>', eliminar_mv.as_view(), name='eliminar-mv'),
   
   
   
   
]