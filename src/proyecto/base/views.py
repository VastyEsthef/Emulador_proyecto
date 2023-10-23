from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Cmaquinas_virtuales

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


class lista_mvs(LoginRequiredMixin, ListView):
   model = Cmaquinas_virtuales
   context_object_name = 'mvs'
   template_name = 'base/mv_list.html'
   

"""class documentacion(LoginRequiredMixin, ListView):
   model = Cmaquinas_virtuales
   context_object_name = 'documentacion'
   template_name = 'base/documentacion_list.html'"""

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
