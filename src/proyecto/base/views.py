from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Ctopology, Cmaquinas_virtuales, Cvirtual_machine

#--------------------- Login / Registro ----------------------

class logueo(LoginView):
   template_name = 'base/login.html'
   fields = '__all__'
   redirect_authenticated_user = True

   def get_success_url(self):
      return reverse_lazy('mvs')


class registro(FormView):
   template_name = 'base/registro.html'
   form_class = UserCreationForm
   redirect_authenticated_user = True
   success_url = reverse_lazy('mvs')

   def form_valid(self,form):
      usuario = form.save()
      return usuario
      #Para hacer que luego del registro mantenga iniciada la sesión
      """if usuario is not None:
         login(self.request, usuario)
      return super(registro, self).form_valid(form)"""

   #Funcion para no mostrar la pagina de registro a un usuario ya logueado
   def get(self, *args, **kwargs):
      if self.request.user.is_authenticated:
         return redirect('mvs')
      return super(registro,self).get(*args, **kwargs)


#--------------------- Topos ----------------------

class list_topologies(ListView):
   model = Ctopology
   context_object_name = 'topologies'
   template_name = 'base/topo_list.html'

   #Nuevo
   def get_queryset(self):
        return Ctopology.objects.all()


class create_topology(CreateView):
   model = Ctopology
   template_name = 'base/topo_form.html'
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


#--------------------- VM ----------------------


class list_vms(ListView):
   model = Cvirtual_machine
   context_object_name = 'vms'
   template_name = 'base/vm_list.html'

   #Nuevo
   def get_queryset(self):
        return Cvirtual_machine.objects.all()


class create_vm(CreateView):
   model = Cvirtual_machine
   template_name = 'base/vm_form.html'
   fields = '__all__'
   success_url = reverse_lazy('vms')

   #Nuevo
   def form_valid(self, form):
        form.instance.save()
        return redirect('vms')


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