<<<<<<< HEAD
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('accounts/', SignUpView.as_view(), name = 'signup'),
=======
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('accounts/', SignUpView.as_view(), name = 'signup'),
>>>>>>> b1ce6284922c8a8069dd4a073bbf381b4b949d18
]