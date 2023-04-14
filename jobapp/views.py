from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Job
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import *

from django.views.generic.edit import UpdateView, DeleteView ,CreateView# new



# Create your views here.


def index(request):
	return render(request,'index.html')


class Home(LoginRequiredMixin,ListView):
	template_name='home.html'
	model=Job
	



class ApplyPage(CreateView):
	template_name='apply.html'
	model=Job
	fields=('name','position','description','salary','Location')

	def form_valid(self, form): # new
		form.instance.user = self.request.user
		return super().form_valid(form)