from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm,ApplyForm
#from .forms import SignUpForm
# Create your views here.

class SignUpPage(CreateView):
	form_class=SignUpForm
	template_name='registration/signupp.html'
	success_url=reverse_lazy('homepage')


def applyPage(request):
    form=ApplyForm()
    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'registration/apply.html',context)