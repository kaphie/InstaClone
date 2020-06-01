from django.shortcuts import get_list_or_404, render, redirect
from django.utils import timezone
from django.urls import reverse
from.forms import PostForm
from .models import Post
from django.views.generic import(
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    RedirectView,
)

from datetime import datetime
from .models import Post 
from .forms import PostForm 

# Create your views here.

class PostlistView(ListView):
    template_name = "insta/post_list.html"
    queryset = Post.objects.all().filter(created_date_lte=timezone.now()).order_by('-created_date')
    context_object_name = 'posts'

class PostCreateView(CreateView):
    template_name = 'insta/post_create.html'
    form_class = PostForm     
    queryset = Post.objects.all()
    #success_url ='/'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    template_name = 'insta/post_deatil.html'
    queryset = Post.objects.all().filter(created_date_lte=timezone.now())

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_list_or_404(Post, id=id_)

class PostUpdateView(UpdateView):
    template_name = 'insta/create.html'
    form_class = PostForm 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

        def form_valid(self, form):
            #form.instance.author = self.request.user 
            return super().form_valid(form) 

class PostDeleteView(DeleteView):
    template_name = 'insta/delete.html'

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def get_success_url(self):
        return reverse('insta:post_list')


def saved_posts(request):
    posts = Post.objects.filter(saved=True)
    context = {'saved_posts': posts}
    return render(request, 'insta/saved_posts.html', context) 


class PostLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        id_ = self.kwargs.get("id")
        obj = get_object_or_404(Post, id=id_)
        url_ = obj.get_absolute_url()
        user = self.request.user 
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user) 
        return url_ 


