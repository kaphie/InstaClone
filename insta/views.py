from django.shortcuts import render, get_list_or_404
from django.utils import timezone
from.forms import PostForm
from .models import Post
from django.views.generic import(
    ListView,
    CreateView,
    DetailView,
)

# Create your views here.

class PostlistView(ListView):
    template_name = "insta/post_list.html"
    queryset = Post.objects.all().filter(created_date_lte=timezone.now()).order_by('-created_date')
    context_object_name = 'posts'

class PostCreateView(CreateView):
    template_name = 'insta/post_create.html'
    form_class = PostForm     
    queryset = Post.objects.all()
    success_url ='/'

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

