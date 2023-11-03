from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Ctopology, Cmaquinas_virtuales, Cvirtual_machine
#---
from openstack_sdk import password_authentication_with_unscoped_authorization, password_authentication_with_scoped_authorization


# Landing Page

def landing_page(request):
   return render(request, 'base/landing_page.html')
   


# AUTHENTICATION SECTION
def get_token_for_admin():
    r = password_authentication_with_scoped_authorization(KEYSTONE_ENDPOINT, ADMIN_USER_DOMAIN_NAME, ADMIN_USERNAME, ADMIN_USER_PASSWORD, DOMAIN_ID, ADMIN_PROJECT_NAME)
    if r.status_code == 201:
        return r.headers['X-Subject-Token']
    else:
        return None


def login(username, password):
    r = password_authentication_with_unscoped_authorization(KEYSTONE_ENDPOINT, DOMAIN_ID, username, password)
    if r.status_code == 201:
        u = r.json()['token']['user']
        user_objetct = User(u['id'],u['name'])
        return user_objetct
    else:
        return None



#--------------------- Login / Registro ----------------------

"""class logueo(LoginView):
   template_name = 'base/login.html'
   fields = '__all__'
   redirect_authenticated_user = True

   #def get_success_url(self):
      #   return reverse_lazy('topologies')


class registro(FormView):
   template_name = 'base/registro.html'
   form_class = UserCreationForm
   redirect_authenticated_user = True
   success_url = reverse_lazy('mvs')

   def form_valid(self,form):
      usuario = form.save()
      return usuario
      #Para hacer que luego del registro mantenga iniciada la sesión
      #if usuario is not None:
      #   login(self.request, usuario)
      #return super(registro, self).form_valid(form)

   #Funcion para no mostrar la pagina de registro a un usuario ya logueado
   def get(self, *args, **kwargs):
      if self.request.user.is_authenticated:
         return redirect('mvs')
      return super(registro,self).get(*args, **kwargs)
"""

#--------------------- Topos ----------------------

class list_topologies(ListView):
   model = Ctopology
   context_object_name = 'topologies'
   template_name = 'base/list_topo.html'

   #Nuevo
   def get_queryset(self):
        return Ctopology.objects.all()


class create_topology(CreateView):
   model = Ctopology
   template_name = 'base/create_topo.html'
   fields = '__all__'
   success_url = reverse_lazy('topologies')

   #Nuevo
   def form_valid(self, form):
        form.instance.save()
        return redirect('topologies')
   

class detail_topology(DetailView):
   model = Ctopology
   context_object_name = 'topology'
   template_name = 'base/topo_detail.html'


class delete_topology(DeleteView):
   model = Ctopology
   context_object_name = 'topology'
   template_name = 'base/delete_topo.html'
   success_url = reverse_lazy('topologies')

#--------------------- VM ----------------------


class list_vms(ListView):
   model = Cvirtual_machine
   context_object_name = 'vms'
   template_name = 'base/list_vm.html'

   #Nuevo
   def get_queryset(self):
        return Cvirtual_machine.objects.all()


class create_vm(CreateView):
   model = Cvirtual_machine
   template_name = 'base/create_vm.html'
   fields = '__all__'
   success_url = reverse_lazy('vms')

   #Nuevo
   def form_valid(self, form):
        form.instance.save()
        return redirect('vms')


class link_vm(CreateView):
   model = Cvirtual_machine
   template_name = 'base/link_vm.html'
   fields = ('name',)
   success_url = reverse_lazy('vms')


#--------------------- MVs OLD - español----------------------

class lista_mvs(LoginRequiredMixin, ListView):
   model = Cmaquinas_virtuales
   context_object_name = 'mvs'
   template_name = 'base/mv_list.html'
   

class crear_mv(LoginRequiredMixin, CreateView):
   model = Cmaquinas_virtuales
   template_name = 'base/mv_form.html'
   fields = '__all__'
   success_url = reverse_lazy('mvs')

class eliminar_mv(LoginRequiredMixin, DeleteView):
   model = Cmaquinas_virtuales
   context_object_name = 'mv'
   template_name = 'base/mv_confirm_delete.html'
   success_url = reverse_lazy('mvs')






"""class documentacion(LoginRequiredMixin, ListView):
   model = Cmaquinas_virtuales
   context_object_name = 'documentacion'
   template_name = 'base/documentacion_list.html'"""