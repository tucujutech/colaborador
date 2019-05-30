from django.conf.urls import url
from.views import *

urlpatterns=[
   url('usernew/', resistrarUsuario, name='usernew'),
   url('login/',Login,name='login'),
   url('dashboard/',dashboard,name='dashboard'),
   url(r'^logout/',deslogar,name='logout'),
   url(r'^colaboradorNew/',ColaboradorNew,name='colaboradorNew'),
   url(r'^listuser/',ListarUsuario,name='listuser'),
]