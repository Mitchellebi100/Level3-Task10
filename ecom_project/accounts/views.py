<<<<<<< HEAD
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


class SignUpView(generic.CreateView):
    '''this is the signup view'''
    form_class    = UserCreationForm
    success_url   = reverse_lazy('login')
=======
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


class SignUpView(generic.CreateView):
    form_class    = UserCreationForm
    success_url   = reverse_lazy('login')
>>>>>>> b1ce6284922c8a8069dd4a073bbf381b4b949d18
    template_name = 'signup.html'