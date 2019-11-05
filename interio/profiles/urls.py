from django.urls import path
from .views import *
from . import views

app_name='profiles'

urlpatterns = [
    path('', Index.as_view(),name='home'),
    path('<int:pk>', PostDetail.as_view(), name='detail'),
    # path('contact', views.contact,name='contact'),
    path('add', views.PostCreate.as_view(),name='create'),
    path('update/<int:pk>', views.PostUpdate.as_view(),name='update'),
    path('delete/<int:pk>', views.PostDelete.as_view(),name='delete'),
    path('register', views.UserFormView.as_view(),name='register'),
    path('contact', views.Contact.as_view(),name='contact'),
    

]