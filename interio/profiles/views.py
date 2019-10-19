from django.shortcuts import render
from django.views import generic
from .models import Post

# # Create your views here.
# def index(request):
#     return render(request,'index.html')

class Index(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()



