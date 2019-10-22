from django.urls import path
from .views import *
from . import views
app_name='profiles'
urlpatterns = [
    path('', Index.as_view(),name='home'),
    path('<int:pk>', PostDetail.as_view(), name='detail'),
    path('contact', views.contact,name='contact'),

]