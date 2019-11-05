from django.shortcuts import render
from django.views import generic
from .models import Post
from django.contrib.auth import views
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail


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


class UserFormView(generic.View):
	form_class = UserForm
	template_name = 'registration/signup.html'	

	#display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	# process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit = False)

			#cleaned (normalised) data

			username_var = form.cleaned_data['username']
			password_var = form.cleaned_data['password']
			email_var = form.cleaned_data['email']
			user.set_password(password_var)
			
			try:
				email_exists = User.objects.get(email = email_var)
				form.add_error('email', 'E-Mail Already Exists')
				return render(request, self.template_name, {'form':form})
			
			except:
				user.save()


				#returns User objects if credentials are correct
				user = authenticate(username = username_var, password = password_var)

				if user is not None:
					if user.is_active:
						login(request, user)
						return redirect('profiles:home')

		return render(request, self.template_name, {'form':form})

class Contact(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('profiles:home')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            send_mail(form.cleaned_data['title'] + " - Query by " + form.cleaned_data['name'] + " - " + form.cleaned_data['email'],
                form.cleaned_data['message'] ,'abhinavmahajan004@gmail.com',
            ['abhinavmahajan1998@gmail.com'], fail_silently=True )
            return self.form_valid(form)
        else:
            return self.form_invalid(form)




    