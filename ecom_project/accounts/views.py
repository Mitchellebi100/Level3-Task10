from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


class SignUpView(generic.CreateView):
    '''this is the signup view'''
    form_class    = UserCreationForm
    success_url   = reverse_lazy('login')
    template_name = 'signup.html'