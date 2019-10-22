from django.shortcuts import render
from django.views import generic
from .models import Post
from django.contrib.auth import views
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import redirect

class Index(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'


class Login(views.LoginView):
    template_name = 'registration/login.html'


class PostCreate(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'postform.html'
    # success_url = reverse_lazy('profiles:home')

    def form_valid(self, form, *args, **kwargs):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        return super(PostCreate, self).form_valid(form, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('profiles:detail', kwargs={'pk' : self.object.pk})

class PostUpdate(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'postform.html'
    success_url = reverse_lazy('profiles:detail')

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('profiles:detail', kwargs={'pk':self.kwargs['pk']})

class PostDelete(generic.DeleteView):
    model = Post
    # template_name = 'postform.html'
    success_url = reverse_lazy('profiles:home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def contact(request):
    return render(request,'contact.html')



    